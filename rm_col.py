import pandas as pd
import os


def remove_column(input_file):
    df = pd.read_excel(input_file)

    # Drop the first three columns
    df.drop(df.columns[[0, 1]], axis=1, inplace=True)

    # Save the modified DataFrame to a new Excel file
    output_file = "vidhan_sabha/" + str(input_file).split("/")[-1]
    df.to_excel(output_file, index=False)

    print(
        f"The first two columns have been removed and the new file is saved as '{output_file}'."
    )


# Read the Excel file into a DataFrame
files = [f for f in os.listdir("static") if f.endswith(".xlsx")]
for file in files:
    remove_column(f"static/{file}")
