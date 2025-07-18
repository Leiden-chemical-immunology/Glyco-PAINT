from __future__ import print_function

import csv
import os
import sys
import time
import shutil

from javax.swing import JFrame, JPanel, JButton, JTextField, JFileChooser, JOptionPane, BorderFactory
from java.lang.System import getProperty

paint_dir = os.path.join(getProperty('fiji.dir'), "Scripts", "Glyco-PAINT")
sys.path.append(paint_dir)

from LoggerConfig import (
    paint_logger_change_file_handler_name)

from FijiSupportFunctions import (
    ask_user_for_file,
    format_time_nicely)

from LoggerConfig import paint_logger

from Run_TrackMate import run_trackmate

# Set an appropriate name for the log file
paint_logger_change_file_handler_name('Run TrackMate Sweep.log')

# Redirect stdout and stderr to suppress output
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

def run_trackmate_batch():

    batch_file_name = ask_user_for_file("Specify the batch file")
    if not batch_file_name:
        paint_logger.info("User aborted the batch processing.")
        sys.exit(1)

    if not os.path.exists(batch_file_name):
        msg = "Error: The file '{}' does not exist.".format(batch_file_name)
        paint_logger.error(msg)
        JOptionPane.showMessageDialog(None, msg, "Warning", JOptionPane.WARNING_MESSAGE)
    else:

        message = "Processing TrackMate batchfile: '{}'".format(batch_file_name)
        paint_logger.info("")
        paint_logger.info("")
        paint_logger.info("-" * len(message))
        paint_logger.info("-" * len(message))
        paint_logger.info("")
        paint_logger.info(message)
        paint_logger.info("")
        paint_logger.info("-" * len(message))
        paint_logger.info("-" * len(message))
        paint_logger.info("")
        paint_logger.info("")

        try:
            # Use `with` to open the file and ensure it is closed after reading
            with open(batch_file_name, mode='r') as file:
                # Create a DictReader object
                csv_reader = csv.DictReader(file)

                # Check if the required columns are present
                required_columns = ['Project', 'Image Source', 'Image', 'Experiment', 'Process']
                if not all(col in csv_reader.fieldnames for col in required_columns):
                    paint_logger.error("Run TrackMate Batch: Missing one or more required columns in batch file: {}".format(required_columns))
                    sys.exit()

                # Read and print each row
                time_stamp_overall = time.time()
                error = False
                for row in csv_reader:
                    print(row)
                    if 'y' in row['Process'].lower():
                        time_stamp = time.time()
                        if not os.path.exists(row['Project']):
                            paint_logger.error("Error: The Project source '{}' does not exist.".format(row['Project']))
                            error = True
                            continue

                        if not os.path.exists(row['Image Source']):
                            paint_logger.error("Error: The Image source '{}' does not exist.".format(row['Image Source']))
                            error = True
                            continue

                        if not os.path.exists(os.path.join(row['Image Source'], row['Image'])):
                            paint_logger.error("Error: The Image source '{}' does not exist.".format(os.path.join(row['Image Source'], row['Image'])))
                            error = True
                            continue

                        source = os.path.join(row['Project'], row['Experiment'])
                        print (source)
                        if not os.path.exists(source):
                            paint_logger.error("Error: The Experiment '{}' does not exist.".format(source))
                            error = True
                            continue

                        message = "Processing experiment '{}'".format(row['Experiment'])
                        paint_logger.info("")
                        paint_logger.info("-" * len(message))
                        paint_logger.info(message)
                        paint_logger.info("-" * len(message))
                        paint_logger.info(os.path.join(row['Project'], row['Experiment']))
                        paint_logger.info(os.path.join(row['Image Source'], row['Experiment']))

                        project_dir = row['Project']
                        experiment = row['Experiment']
                        experiment_dir = os.path.join(project_dir, experiment)
                        image_dir = os.path.join(row['Image Source'], row['Image'])
                        default_json_path = os.path.expanduser('~/Paint/Defaults')

                        # Paths for copy operations
                        src_json = os.path.join(experiment_dir, 'Paint.json')
                        backup_json = os.path.join(default_json_path, 'Paint-Keep.json')
                        dst_json = os.path.join(default_json_path, 'Paint.json')

                        # 1. Backup existing Paint.json (if any)
                        paint_logger.info("Backing up Paint.json from {} to {}".format(dst_json, backup_json))
                        if os.path.exists(dst_json):
                            shutil.copy(dst_json, backup_json)

                        # 2. Copy experiment's Paint.json to Defaults
                        paint_logger.info("Copying Paint.json from {} to {}".format(src_json, dst_json))
                        shutil.copy(src_json, dst_json)

                        # 3. Run TrackMate
                        run_trackmate(
                            experiment_directory=experiment_dir,
                            recording_source_directory=image_dir,
                            convert=False,
                            case_text = experiment
                        )

                        # 4. Restore original Paint.json
                        if os.path.exists(backup_json):
                            paint_logger.info("Restoring original Paint.json from {} to {}".format(backup_json, dst_json))
                            shutil.copy(backup_json, dst_json)

                        paint_logger.info("Processing completed in {} seconds".format(format_time_nicely(time.time() - time_stamp)))
                        paint_logger.info("")
                        paint_logger.info("")

                run_time = round(time.time() - time_stamp_overall, 1)

                if error:
                    msg = "Errors occurred during processing. Refer to the log file for more information."
                    JOptionPane.showMessageDialog(None, msg, "Warning", JOptionPane.WARNING_MESSAGE)
                else:
                    paint_logger.info("Processing completed in {} seconds".format(format_time_nicely(run_time)))

        except csv.Error as e:
            paint_logger.error("run_trackmate_batch: Error reading CSV file: {}".format(e))
        except Exception as e:
            paint_logger.error("run_trackmate_batch: An unexpected error occurred: {}".format(e))


if __name__ == '__main__':
    run_trackmate_batch()