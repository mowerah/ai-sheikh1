import pandas as pd
from glob import glob

# --------------------------------------------------------------
# Define paths and filenames
# --------------------------------------------------------------

output_path = "../../data/processed/"

# Load the data
data_files = glob(output_path + "Processed_School_Data.csv")
df = pd.read_csv(data_files[0])
df['epoch (ms)'] = pd.to_datetime(df['epoch (ms)'])

# Filter rows where school is 'Maplewood Academy'
maplewood_students = df.loc[df['school'] == 'Maplewood Academy']
print(maplewood_students)
