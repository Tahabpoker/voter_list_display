# import pandas as pd # type: ignore 

# head =[ "Sr No",	"List No",	"Electoral Name,"	"Relative Name",	"Address" ," School",	"Age",	"Gender",	"Epic No", "Is Photo"]
# # Read the Excel file into a data frame
# df = pd.read_excel('./static/voters_list.xlsx', names=head)

# # data_name_lower = 152
# # data_column = "List No"

# # # data_name_lower = data_name.lower()
# # df_column_lower = df[data_column].str.lower()

# # df[data_name_lower] = df[data_name_lower].astype(str)   

# # apple_rows = df[data_column == data_name_lower]

# print(df[df["List No"] == 152])


# # print(apple_rows.to_html())
# # print(df)



# # data_name = "2"
# # data_column = "1"

# # data_name_lower = data_name.lower()
# # df_column_lower = df[data_column].str.lower()

# # apple_rows = df[df_column_lower == data_name_lower]

# # print(apple_rows)

















# # data_name = "England"

# # # Search for the value in the first column (assuming "Bar" is the first column)
# # apple_rows = df[1 == data_name]

# # if not apple_rows.empty:
# #     # Extract the first row as a Series (single row)
# #     first_row_data = apple_rows.iloc[0]

# #     # Access individual cell values using column names
# #     cell1_value = first_row_data['Bar']  # Access by column name 'Bar'
# #     cell2_value = first_row_data['text']  # Assuming 'Food' is the second column name
# #     cell3_value = first_row_data['Foo']  # Assuming 'Third_Column' is the third column name

# #     # Display results
# #     print("Cell 1 value:", cell1_value)
# #     print("Cell 2 value:", cell2_value)
# #     print("Cell 3 value:", cell3_value)

# # else:
# #     print("Value '{}' not found in the first column.".format(data_name))











for i in range(152,187):
    print(f"<option value= '{i}'>{i}</option>")