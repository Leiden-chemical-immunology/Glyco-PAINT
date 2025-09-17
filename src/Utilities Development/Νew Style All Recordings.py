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
            if 'All Recordings' in file and file.endswith('.csv'):
                file_path = os.path.join(root, file)

                try:
                    # Read the CSV file
                    df = pd.read_csv(file_path, low_memory=False)

                    df.drop(columns=['Case', 'Min Tracks for Tau', 'Min Spots in Track', 'Min Required R Squared', 'Nr of Squares in Row', 'Max Allowable Variability', 'Min Required Density Ratio'], inplace=True, errors='ignore')

                    safe_rename(df,{"Nr Spots": "Number of Spots",
                                               "Nr Tracks": "Number of Tracks",
                                               "Probe" :"Probe Name",
                                               "Condition Nr": "Condition Number",
                                               "Replicate Nr": "Replicate Number",
                                               "Nr Spots in All Tracks": "Number of Spots in All Tracks",
                                               "Number Of Spots In All Tracks" : "Number of Spots in All Tracks",
                                               "Process" : "Process Flag"})



                    df = df[[
                        "Recording Name",
                        "Condition Number",
                        "Replicate Number",
                        "Probe Name",
                        "Probe Type",
                        "Cell Type",
                        "Adjuvant",
                        "Concentration",
                        "Process Flag",
                        "Threshold",
                        "Number of Spots",
                        "Number of Tracks",
                        "Run Time",
                        "Recording Size",
                        "Time Stamp",
                        "Number of Spots in All Tracks",
                        "Exclude",
                        "Tau",
                        "R Squared",
                        "Density"
                    ]]

                    # Define mapping
                    true_values = {'yes', 'y'}
                    false_values = {'no', 'n'}

                    def normalize_flag(val):
                        if pd.isna(val) or str(val).strip() == "":
                            return True
                        val = str(val).strip().lower()
                        if val in true_values:
                            return True
                        elif val in false_values:
                            return False
                        else:
                            return None  # or False if you prefer

                    df['Process Flag'] = df['Process Flag'].map(normalize_flag)



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
