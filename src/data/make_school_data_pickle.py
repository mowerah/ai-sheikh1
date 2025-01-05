import pandas as pd
from glob import glob

# --------------------------------------------------------------
# Define paths and filenames
# --------------------------------------------------------------
data_path = "../../data/raw/school_data/"
# output_path = "../../data/processed/"
output_path = "../../data/interim/"

# Implement functions to make the code modular
files = glob(data_path + "*.csv")


def read_data_from_csv_files(files):
    # --------------------------------------------------------------
    # Initialize empty DataFrame for processed data
    # --------------------------------------------------------------
    processed_df = pd.DataFrame()

    # --------------------------------------------------------------
    # Process each file
    # --------------------------------------------------------------
    for f in files:
        try:
            # Extract features from filename
            file_name = f.split("/")[-1]
            school = "".join(
                [
                    " " + char if char.isupper() else char
                    for char in file_name.split("_")[0]
                ]
            ).strip()
            category = "GCSE" if "GCSE" in file_name else "A-level"
            year = file_name.split("_")[2].replace(".csv", "")

            # Read the CSV file
            df = pd.read_csv(f)

            # Standardize column names
            df.columns = [col.strip().lower() for col in df.columns]

            # Ensure required columns exist
            required_columns = {"epoch (ms)", "time (01:00)", "elapsed (s)"}
            if not required_columns.issubset(df.columns):
                print(
                    f"Skipping {f}: Missing required columns {required_columns - set(df.columns)}"
                )
                continue

            # Add derived columns
            df["school"] = school
            df["category"] = category
            df["year"] = year

            # Set datetime index
            df.index = pd.to_datetime(df["epoch (ms)"], unit="ms")

            # Drop unnecessary columns
            df.drop(columns=["epoch (ms)", "time (01:00)", "elapsed (s)"], inplace=True)

            # Append to the processed DataFrame
            processed_df = pd.concat([processed_df, df], ignore_index=False)

        except Exception as e:
            print(f"Error processing file {f}: {e}")

    return processed_df


def save_processed_df_to_pickle_file(processed_df):
    # --------------------------------------------------------------
    # Export processed dataset
    # --------------------------------------------------------------
    # processed_output_file = output_path + "Processed_School_Data_W_Functions.csv"
    # print(processed_output_file)
    # try:
    #     processed_df.to_csv(processed_output_file, index=True)
    #     print("Data processing complete. Processed file saved to:")
    #     print(processed_output_file)
    # except Exception as e:
    #     print(f"Error saving processed data: {e}")

    processed_output_file = output_path + "Processed_School_Data_W_Functions.pkl"
    print(processed_output_file)
    try:
        processed_df.to_pickle(processed_output_file)
        print("Data processing complete. Processed file saved to:")
        print(processed_output_file)
    except Exception as e:
        print(f"Error saving processed data: {e}")


# Call the functions
processed_df = read_data_from_csv_files(files)
if not processed_df.empty:
    save_processed_df_to_pickle_file(processed_df)
else:
    print("No data was processed. Please check the input files.")