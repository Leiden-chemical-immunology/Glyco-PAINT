import pandas as pd
from pathlib import Path

# starting directory (change to your root experiment path)
root = Path("/Users/hans/Paint Test Project")

# the file you want to edit in each subdirectory
target_file = "Experiment Info.csv"

# columns to delete
drop_cols = ["Recording Sequence Nr", "Experiment Date", "Experiment Name"]

# renaming map
rename_map = {
    "Condition Nr": "Condition Number",
    "Replicate Nr": "Replicate Number",
    "Process": "Process Flag",
    "Probe": "Probe Name"
}

for subdir in root.iterdir():
    if subdir.is_dir():
        csv_path = subdir / target_file
        if csv_path.exists():
            print(f"Editing: {csv_path}")

            # read csv
            df = pd.read_csv(csv_path)

            # drop unwanted columns (ignore if missing)
            df = df.drop(columns=[c for c in drop_cols if c in df.columns])

            # rename columns
            df = df.rename(columns=rename_map)

            # ensure all values in Process Flag are True
            if "Process Flag" in df.columns:
                df["Process Flag"] = True

            # swap Process Flag and Threshold columns
            if "Process Flag" in df.columns and "Threshold" in df.columns:
                cols = df.columns.tolist()
                i_flag = cols.index("Process Flag")
                i_thresh = cols.index("Threshold")
                # swap positions
                cols[i_flag], cols[i_thresh] = cols[i_thresh], cols[i_flag]
                df = df[cols]

            # write back to disk (overwrite)
            df.to_csv(csv_path, index=False)

print("Done.")