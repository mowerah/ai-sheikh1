# Import required libraries
import pandas as pd
from glob import glob

data_path = "../../data/raw/school_data/"
output_path = "../../data/processed/"
files = glob(data_path + "*.csv")

def read_data_from_csv_files(files):
    # Initialize an empty DataFrame
    processed_df = pd.DataFrame()

    # Iterate over files
    for f in files:
        try:
            # Extract metadata from filename
            file_name = f.split("/")[-1]
            school = ''.join([
                " " + char if char.isupper() else char
                for char in file_name.split("_")[0]
            ]).strip()
            category = "GCSE" if "GCSE" in file_name else "A-level"
            year = file_name.split("_")[2].replace(".csv", "")

            # Read data
            df = pd.read_csv(f)
            df.columns = [col.strip().lower() for col in df.columns]

            # Validate required columns
            required_columns = {"epoch (ms)", "time (01:00)", "elapsed (s)"}
            if not required_columns.issubset(df.columns):
                continue

            # Add metadata
            df["school"] = school
            df["category"] = category
            df["year"] = year
            df.index = pd.to_datetime(df["epoch (ms)"], unit="ms")
            df.drop(columns=["epoch (ms)", "time (01:00)", "elapsed (s)"],
                    inplace=True)

            # Append to processed DataFrame
            processed_df = pd.concat([processed_df, df], ignore_index=False)
        except Exception as e:
            print("Error processing file", f, ":", e)

    return processed_df


def save_processed_df_to_file(processed_df):
    processed_output_file = output_path + "Processed_School_Data2.csv"
    try:
        processed_df.to_csv(processed_output_file, index=True)
        print("Data saved to:", processed_output_file)
    except Exception as e:
        print("Error saving data:", e)


processed_df = read_data_from_csv_files(files)
if not processed_df.empty:
    save_processed_df_to_file(processed_df)
else:
    print("No data processed.")
