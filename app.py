# app.py
import pandas as pd #type: ignore
from flask import Flask, render_template, request #type: ignore

# Read the Excel file into a data frame
df = pd.read_excel('./static/voters_list.xlsx')

# Flask constructor
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # User submitted the form
        data_name = request.form.get('data_name')
        data_column = request.form.get('data_column')

        if data_name and (data_column ==  "Electoral Name" or "Relative Name" or "Epic No") :
            # Convert search value and column values to lowercase
            data_name_lower = data_name.lower()
            df_column_lower = df[data_column].str.lower()

            # Search for the value in the specified column (case-insensitive)
            apple_rows = df[df_column_lower == data_name_lower]

            if not apple_rows.empty:
                # Extract the first row as a Series (single row)
                first_row_data = apple_rows.iloc[0]

                # Access individual cell values using column names
                cell1_value = first_row_data['Sr No']#
                cell2_value = first_row_data['List No']#
                cell3_value = first_row_data['Electoral Name']#
                cell4_value = first_row_data['Relative Name']#
                cell5_value = first_row_data['Address']#
                cell6_value = first_row_data['School']#
                cell7_value = first_row_data['Age']#
                cell8_value = first_row_data['Gender']#
                cell9_value = first_row_data['Epic No']#
                

                # Render the HTML template with the cell values
                return render_template('index.html', cell1_value=cell1_value, cell2_value=cell2_value, cell3_value=cell3_value, cell4_value=cell4_value, cell5_value=cell5_value, cell6_value=cell6_value, cell7_value=cell7_value, cell8_value=cell8_value, cell9_value=cell9_value)
            else:
                error_message = "Value '{}' not found in the specified column '{}'".format(data_name, data_column)
                return render_template('index.html', error_message=error_message)
            
        elif data_name and (data_column == "Sr No" or "List No" or "Gender" or "Age" or "Address" or "School"):
            data_name_lower = data_name.lower()
            df_column_lower = df[data_column].str.lower()

            apple_rows = df[df_column_lower == data_name_lower]
            # apple_rows = pd.read_excel("voter_list_data_1.xlsx")
            # rows_to_html = apple_rows.to_html()
            return render_template('print_excel_table.html',  tables =[apple_rows.to_html(classes='data', header="true")])

        else:
            error_message = "Please provide both a value and select a column."
            return render_template('index.html', error_message=error_message)

    # User accessed the page (GET request)
    return render_template('index.html', cell1_value="", cell2_value="", cell3_value="")

if __name__ == '__main__':
    app.run(debug=True)



















# # app.py

# import pandas as pd
# from flask import Flask, render_template, request

# # Read the Excel file into a data frame
# df = pd.read_excel('excel.xlsx')

# # Flask constructor
# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # User submitted the form
#         data_name = request.form.get('data_name')
#         data_column = request.form.get('data_column')

#         if data_name and data_column:
#             # Search for the value in the specified column
#             apple_rows = df[df[data_column] == data_name]

#             if not apple_rows.empty:
#                 # Extract the first row as a Series (single row)
#                 first_row_data = apple_rows.iloc[0]

#                 # Access individual cell values using column names
#                 cell1_value = first_row_data['Bar']
#                 cell2_value = first_row_data['text']
#                 cell3_value = first_row_data['Foo']

#                 # Render the HTML template with the cell values
#                 return render_template('index.html', cell1_value=cell1_value, cell2_value=cell2_value, cell3_value=cell3_value)
#             else:
#                 error_message = "Value '{}' not found in the specified column '{}'".format(data_name, data_column)
#                 return render_template('index.html', error_message=error_message)
#         else:
#             error_message = "Please provide both a value and select a column."
#             return render_template('index.html', error_message=error_message)

#     # User accessed the page (GET request)

#     # User accessed the page (GET request)
#     return render_template('index.html', cell1_value="", cell2_value="", cell3_value="")

# if __name__ == '__main__':
#     app.run(debug=True)









# app.py

# import pandas as pd
# from flask import Flask, render_template, request

# # Read the Excel file into a data frame
# df = pd.read_excel('excel.xlsx')

# # Flask constructor
# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # User submitted the form
#         data_name = request.form.get('data_name')
#         data_column = request.form.get('data_column')

#         if data_name and data_column:
#             # Search for the value in the specified column
#             apple_rows = df[df[data_column] == data_name]

#             if not apple_rows.empty:
#                 # Extract the first row as a Series (single row)
#                 first_row_data = apple_rows.iloc[0]

#                 # Access individual cell values using column names
#                 cell1_value = first_row_data['Bar']
#                 cell2_value = first_row_data['text']
#                 cell3_value = first_row_data['Foo']

#                 # Render the HTML template with the cell values
#                 return render_template('index.html', cell1_value=cell1_value, cell2_value=cell2_value, cell3_value=cell3_value)
#             else:
#                 return "Value '{}' not found in the specified column '{}' ".format(data_name,data_column)
#         else:
#             return "Please provide both a value and select a column."

#     # User accessed the page (GET request)
#     return render_template('index.html', cell1_value="", cell2_value="", cell3_value="")

# if __name__ == '__main__':
#     app.run(debug=True)

