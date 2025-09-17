import os

import pandas as pd

def safe_rename(df: pd.DataFrame, rename_map: dict, inplace: bool = True) -> pd.DataFrame:
    """
    Safely rename columns in a DataFrame.
    Only renames columns that exist, ignoring the rest.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to modify
    rename_map : dict
        Mapping of old_name -> new_name
    inplace : bool, default True
        If True, modify the DataFrame in-place and return it.
        If False, return a new DataFrame.

    Returns
    -------
    pd.DataFrame
        The DataFrame with renamed columns
    """
    valid_map = {k: v for k, v in rename_map.items() if k in df.columns}
    return df.rename(columns=valid_map, inplace=inplace) or df


def update_csv_columns(directory):
    # Traverse the directory tree
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file is a CSV file
            if 'All Squares' in file and file.endswith('.csv'):
                file_path = os.path.join(root, file)

                try:
                    # Read the CSV file
                    df = pd.read_csv(file_path, low_memory=False)

                    df.drop(columns=['Recording Sequence Nr', 'Experiment Name', 'Experiment Date', 'Condition Nr', 'Replicate Nr', 'Probe', 'Probe Type', 'Cell Type', 'Adjuvant', 'Concentration', 'Threshold'], inplace=True, errors='ignore')

                    safe_rename(df, {"Square Nr": "Square Number",
                                     "Row Nr": "Row Number",
                                     "Col Nr": "Column Number",
                                     "Col Number": "Column Number",
                                     "Label Nr": "Label Number",
                                     "Square Nr": "Square Number",
                                     "Nr Tracks": "Number of Tracks",
                                     "Ext Recording Name": "Recording Name",
                                     "Cell Id": "Cell ID"})

                    df['Mean Long Track Duration'] = -1
                    df['Mean Short Track Duration'] = -1


                    df = df[[
                        "Unique Key",
                        "Recording Name",
                        "Square Number",
                        "Row Number",
                        "Column Number",
                        "Label Number",
                        "Cell ID",

                        "Selected",
                        "Square Manually Excluded",
                        "Image Excluded",

                        "X0",
                        "Y0",
                        "X1",
                        "Y1",

                        "Number of Tracks",
                        "Variability",
                        "Density",
                        "Density Ratio",
                        "Tau",
                        "R Squared",

                        "Median Diffusion Coefficient",
                        "Mean Diffusion Coefficient",

                        "Median Diffusion Coefficient Ext",
                        "Mean Diffusion Coefficient Ext",

                        "Median Long Track Duration",
                        "Mean Long Track Duration",

                        "Median Short Track Duration",
                        "Mean Short Track Duration",

                        "Median Displacement",
                        "Max Displacement",
                        "Total Displacement",

                        "Median Max Speed",
                        "Max Max Speed",

                        "Median Mean Speed",
                        "Max Mean Speed",

                        "Max Track Duration",
                        "Total Track Duration",
                        "Median Track Duration"
                    ]]

                    # Save the updated DataFrame back to the same CSV file
                    df.to_csv(file_path, index=False)
                    print(f"File saved: {file_path}")

                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")


# Usage: Replace 'your_directory_path' with the path of the directory you want to traverse
directory = '/Users/hans/Downloads/Paint Data - v38'

update_csv_columns(directory)


def safe_rename(df: pd.DataFrame, rename_map: dict, inplace: bool = True) -> pd.DataFrame:
    """
    Safely rename columns in a DataFrame.
    Only renames columns that exist, ignoring the rest.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to modify
    rename_map : dict
        Mapping of old_name -> new_name
    inplace : bool, default True
        If True, modify the DataFrame in-place and return it.
        If False, return a new DataFrame.

    Returns
    -------
    pd.DataFrame
        The DataFrame with renamed columns
    """
    valid_map = {k: v for k, v in rename_map.items() if k in df.columns}
    return df.rename(columns=valid_map, inplace=inplace) or df
