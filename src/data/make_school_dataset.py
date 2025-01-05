import pandas as pd
from glob import glob

data_path = "../../data/raw/school_data/"
output_path = "../../data/processed/"
files = glob(data_path + "*.csv")

processed_df = pd.DataFrame()

for f in files:
    file_name = f.split("/")[-1]
    school = file_name.split("_")[0]
    school = ''.join(
        [" " + char if char.isupper() else char for char in school]).strip()
    category = "GCSE" if "GCSE" in file_name else "A-level"
    year = file_name.split("_")[2].replace(".csv", "")

    df = pd.read_csv(f)
    df["school"] = school
    df["category"] = category
    df["year"] = year
    processed_df = pd.concat([processed_df, df], ignore_index=True)

processed_output_file = output_path + "Processed_School_Data.csv"
processed_df.to_csv(processed_output_file, index=False)

print("Data processing complete. Processed file saved to:")
print(processed_output_file)
