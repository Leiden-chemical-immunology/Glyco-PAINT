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
            if 'All Tracks' in file and file.endswith('.csv'):
                file_path = os.path.join(root, file)

                try:
                    # Read the CSV file
                    df = pd.read_csv(file_path, low_memory=False)

                    safe_rename(df,{
                                   "Ext Recording Name": "Recording Name",
                                   "Square Nr": "Square Number",
                                   "Label Nr": "Label Number",
                                   "Nr Spots": "Number of Spots",
                                   "Nr Gaps": "Number of Gaps"})


                    df = df[[
                        "Unique Key",
                        "Recording Name",
                        "Track Id",
                        "Track Label",
                        "Number of Spots",
                        "Number of Gaps",
                        "Longest Gap",
                        "Track Duration",
                        "Track X Location",
                        "Track Y Location",
                        "Track Displacement",
                        "Track Max Speed",
                        "Track Median Speed",
                        "Track Mean Speed",
                        "Track Max Speed Calc",
                        "Track Median Speed Calc",
                        "Track Mean Speed Calc",
                        "Diffusion Coefficient",
                        "Diffusion Coefficient Ext",
                        "Total Distance",
                        "Confinement Ratio",
                        "Square Number",
                        "Label Number"
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
