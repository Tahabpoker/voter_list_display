# app.py

import pandas as pd
from flask import Flask, render_template, request

# Read the Excel file into a data frame
df = pd.read_excel('excel.xlsx')

# Flask constructor
app = Flask(__name__)

@app.route('/')
def index():
    # Get user input from the query parameter 'data_name'
    data_name = request.args.get('data_name')

    if data_name:
        # Get the selected data column from the query parameter 'data_column'
        data_column = request.args.get('data_column', default='Bar')

        # Search for the value in the specified column
        apple_rows = df[df[data_column] == data_name]

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
            return "Value '{}' not found in the specified column.".format(data_name)
    else:
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

# @app.route('/')
# def index():
#     # Get user input from the query parameter 'data_name'
#     data_name = request.args.get('data_name')

#     if data_name:
#         # Search for the value in the first column ('Bar')
#         apple_rows = df[df['Bar'] == data_name]

#         if not apple_rows.empty:
#             # Extract the first row as a Series (single row)
#             first_row_data = apple_rows.iloc[0]

#             # Access individual cell values using column names
#             cell1_value = first_row_data['Bar']
#             cell2_value = first_row_data['text']
#             cell3_value = first_row_data['Foo']

#             # Render the HTML template with the cell values
#             return render_template('index.html', cell1_value=cell1_value, cell2_value=cell2_value, cell3_value=cell3_value)
#         else:
#             return "Value '{}' not found in the first column.".format(data_name)
#     else:
#          return render_template('index.html', cell1_value="", cell2_value="", cell3_value="")

# if __name__ == '__main__':
#     app.run(debug=True)






# import pandas as pd  # type: ignore
# from flask import Flask, render_template, request

# # Flask application initialization
# app = Flask(__name__)

# # Route for the main page with a form and dynamic content
# @app.route("/", methods=["GET", "POST"])  # Allow both GET and POST methods
# def index():
#     data_name = request.args.get("data_name")  # Access data name from query string
#     cell1 = None
#     cell2 = None
#     cell3 = None

#     print(data_name)

#     # Process the data name if provided (optional)
#     if data_name:
#         try:
#             df = pd.read_excel("excel.xlsx")
#             apple_rows = df[df.iloc[:, 0] == data_name]
#             if not apple_rows.empty:
#                 first_row_data = apple_rows.iloc[0]
#                 cell1_value = first_row_data['Bar']  # Access by column name 'Bar'
#                 cell2_value = first_row_data['text']  # Assuming 'Food' is the second column name
#                 cell3_value = first_row_data['Foo']

#         except FileNotFoundError:
#             # Handle file not found error (optional)
#             pass  # Or provide an error message for the user

#     # Render the single HTML template with data (or None if not found)
#     return render_template("app.html", data_name=data_name, cell1=cell1, cell2=cell2, cell3=cell3)

# # Run the application
# if __name__ == "__main__":
#     app.run(debug=True)
