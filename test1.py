import pandas as pd

# Read the existing Excel file
df = pd.read_excel('data.xlsx')

# Get input from the user
new_data = {
    'first_name': input('Enter first name: '),
    'last_name': input('Enter last name: '),
    'age': int(input('Enter age: '))
}

# Append the new data to the DataFrame
df = df._append(new_data, ignore_index=True)

# Save the DataFrame back to the Excel file
df.to_excel('data.xlsx', index=False)