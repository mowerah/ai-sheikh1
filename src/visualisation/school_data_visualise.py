import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from IPython.display import display

# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------
df = pd.read_pickle("../../data/interim/Processed_School_Data_W_Functions.pkl")
df = df.set_index("name")
# --------------------------------------------------------------
# Plot single columns
# --------------------------------------------------------------
# plt.plot(df["study_hours_per_week"].reset_index(drop=True))

# --------------------------------------------------------------
# Plot all exercises
# --------------------------------------------------------------
for category in df["category"].unique():
    category_df = df[df["category"] == category]
    display(category_df)
    plt.subplots()
    # plt.plot(category_df["study_hours_per_week"],label=category)
    # plt.figure(figsize=(10, 8))
    plt.plot(
        category_df["study_hours_per_week"],
        marker="o",
        linestyle="-",
        label=category,
        color="green",
    )
    # plt.plot(category_df["study_hours_per_week"].reset_index(drop=True), label=category)
    plt.title(f"Study Hours per Week - {category}")
    plt.xlabel("Student Names")
    plt.ylabel("Study Hours")
    plt.xticks(rotation=45, ha="right")
    # plt.legend()
    plt.tight_layout()
    plt.show()

# --------------------------------------------------------------
# Adjust plot settings
# --------------------------------------------------------------

# --------------------------------------------------------------
# Compare medium vs. heavy sets
# --------------------------------------------------------------

# --------------------------------------------------------------
# Compare participants
# --------------------------------------------------------------

# --------------------------------------------------------------
# Plot multiple axis
# --------------------------------------------------------------

# --------------------------------------------------------------
# Create a loop to plot all combinations per sensor
# --------------------------------------------------------------

# --------------------------------------------------------------
# Combine plots in one figure
# --------------------------------------------------------------

# --------------------------------------------------------------
# Loop over all combinations and export for both sensors
# --------------------------------------------------------------
