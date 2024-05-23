# app.py

import pandas as pd
from flask import Flask, render_template, request

# Read the Excel file into a data frame
df = pd.read_excel('excel.xlsx')

# Flask constructor
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # User submitted the form
        data_name = request.form.get('data_name')
        data_column = request.form.get('data_column')

        if data_name and (data_column == "Bar" or data_column == "Foo" ) :
            # Convert search value and column values to lowercase
            data_name_lower = data_name.lower()
            df_column_lower = df[data_column].str.lower()

            # Search for the value in the specified column (case-insensitive)
            apple_rows = df[df_column_lower == data_name_lower]

            if not apple_rows.empty:
                # Extract the first row as a Series (single row)
                first_row_data = apple_rows.iloc[0]

                # Access individual cell values using column names
                cell1_value = first_row_data['Bar']
                cell2_value = first_row_data['text']
                cell3_value = first_row_data['Foo']

                # Render the HTML template with the cell values
                return render_template('index.html', cell1_value=cell1_value, cell2_value=cell2_value, cell3_value=cell3_value)
            else:
                error_message = "Value '{}' not found in the specified column '{}'".format(data_name, data_column)
                return render_template('index.html', error_message=error_message)
            
        elif data_name and data_column == "text":
            data_name_lower = data_name.lower()
            df_column_lower = df[data_column].str.lower()

            apple_rows = df[df_column_lower == data_name_lower]
            # rows_to_html = apple_rows.to_html()

            return render_template('print_excel_table.html',  tables=[apple_rows.to_html(classes='data', header="true")])

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

