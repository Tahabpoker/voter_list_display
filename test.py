import pandas as pd # type: ignore 

# Read the Excel file into a data frame
df = pd.read_excel('excel.xlsx')

data_name = "England"

# Search for the value in the first column (assuming "Bar" is the first column)
apple_rows = df[df['Bar'] == data_name]

if not apple_rows.empty:
    # Extract the first row as a Series (single row)
    first_row_data = apple_rows.iloc[0]

    # Access individual cell values using column names
    cell1_value = first_row_data['Bar']  # Access by column name 'Bar'
    cell2_value = first_row_data['text']  # Assuming 'Food' is the second column name
    cell3_value = first_row_data['Foo']  # Assuming 'Third_Column' is the third column name

    # Display results
    print("Cell 1 value:", cell1_value)
    print("Cell 2 value:", cell2_value)
    print("Cell 3 value:", cell3_value)

else:
    print("Value '{}' not found in the first column.".format(data_name))
