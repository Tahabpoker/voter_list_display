# app.py
import pandas as pd  # type: ignore
from flask import Flask, render_template, request  # type: ignore

# Read the Excel file into a data frame
df_152 = pd.read_excel("./static/152.xlsx")
df_153 = pd.read_excel("./static/153.xlsx")
df_154 = pd.read_excel("./static/154.xlsx")
df_155 = pd.read_excel("./static/155.xlsx")
df_156 = pd.read_excel("./static/156.xlsx")
df_157 = pd.read_excel("./static/157.xlsx")
df_158 = pd.read_excel("./static/158.xlsx")
df_159 = pd.read_excel("./static/159.xlsx")
df_160 = pd.read_excel("./static/160.xlsx")
df_161 = pd.read_excel("./static/161.xlsx")
df_162 = pd.read_excel("./static/162.xlsx")
df_163 = pd.read_excel("./static/163.xlsx")
df_164 = pd.read_excel("./static/164.xlsx")
df_165 = pd.read_excel("./static/165.xlsx")
df_166 = pd.read_excel("./static/166.xlsx")
df_167 = pd.read_excel("./static/167.xlsx")
df_168 = pd.read_excel("./static/168.xlsx")
df_169 = pd.read_excel("./static/169.xlsx")
df_170 = pd.read_excel("./static/170.xlsx")
df_171 = pd.read_excel("./static/171.xlsx")
df_172 = pd.read_excel("./static/172.xlsx")
df_173 = pd.read_excel("./static/173.xlsx")
df_174 = pd.read_excel("./static/174.xlsx")
df_175 = pd.read_excel("./static/175.xlsx")
df_176 = pd.read_excel("./static/176.xlsx")
df_177 = pd.read_excel("./static/177.xlsx")
df_178 = pd.read_excel("./static/178.xlsx")
df_179 = pd.read_excel("./static/179.xlsx")
df_180 = pd.read_excel("./static/180.xlsx")
df_181 = pd.read_excel("./static/181.xlsx")
df_182 = pd.read_excel("./static/182.xlsx")
df_183 = pd.read_excel("./static/183.xlsx")
df_184 = pd.read_excel("./static/184.xlsx")
df_185 = pd.read_excel("./static/185.xlsx")
df_186 = pd.read_excel("./static/186.xlsx")
df_187 = pd.read_excel("./static/187.xlsx")


# Flask constructor
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    # user submitted form
    data_name = request.form.get("data_name")
    data_column = request.form.get("data_column")
    vidhan_Sabha = request.form.get("vidhan_Sabha")

    match vidhan_Sabha:
        case "152":
            vidhan_Sabha = 152
        case "153":
            vidhan_Sabha = 153
        case "154":
            vidhan_Sabha = 154
        case "155":
            vidhan_Sabha = 155
        case "156":
            vidhan_Sabha = 156
        case "157":
            vidhan_Sabha = 157
        case "158":
            vidhan_Sabha = 158
        case "159":
            vidhan_Sabha = 159
        case "160":
            vidhan_Sabha = 160
        case "161":
            vidhan_Sabha = 161
        case "162":
            vidhan_Sabha = 152
        case "163":
            vidhan_Sabha = 153
        case "164":
            vidhan_Sabha = 154
        case "165":
            vidhan_Sabha = 155
        case "166":
            vidhan_Sabha = 156
        case "167":
            vidhan_Sabha = 157
        case "168":
            vidhan_Sabha = 158
        case "169":
            vidhan_Sabha = 159
        case "160":
            vidhan_Sabha = 160
        case "171":
            vidhan_Sabha = 161
        case "172":
            vidhan_Sabha = 152
        case "173":
            vidhan_Sabha = 153
        case "174":
            vidhan_Sabha = 154
        case "175":
            vidhan_Sabha = 155
        case "176":
            vidhan_Sabha = 156
        case "177":
            vidhan_Sabha = 157
        case "178":
            vidhan_Sabha = 158
        case "179":
            vidhan_Sabha = 159
        case "180":
            vidhan_Sabha = 160
        case "181":
            vidhan_Sabha = 161
        case "182":
            vidhan_Sabha = 152
        case "183":
            vidhan_Sabha = 153
        case "184":
            vidhan_Sabha = 154
        case "185":
            vidhan_Sabha = 155
        case "186":
            vidhan_Sabha = 156
        case "187":
            vidhan_Sabha = 157

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # User submitted the form
#         data_name = request.form.get('data_name')
#         data_column = request.form.get('data_column')

#         if data_name and (data_column ==  "Electoral Name" or "Relative Name" or "Epic No") :
#             # Convert search value and column values to lowercase
#             data_name_lower = data_name.lower()
#             df_column_lower = df[data_column].str.lower()

#             # Search for the value in the specified column (case-insensitive)
#             apple_rows = df[df_column_lower == data_name_lower]

#             if not apple_rows.empty:
#                 # Extract the first row as a Series (single row)
#                 first_row_data = apple_rows.iloc[0]

#                 # Access individual cell values using column names
#                 cell1_value = first_row_data['Electoral Name']#
#                 cell2_value = first_row_data['Relative Name']#
#                 cell3_value = first_row_data['Address']#
#                 cell4_value = first_row_data['School']#
#                 cell5_value = first_row_data['Epic No']#


#                 # Render the HTML template with the cell values
#                 return render_template('index.html', cell1_value=cell1_value, cell2_value=cell2_value, cell3_value=cell3_value, cell4_value=cell4_value, cell5_value=cell5_value)
#             else:
#                 error_message = "Value '{}' not found in the specified column '{}'".format(data_name, data_column)
#                 return render_template('index.html', error_message=error_message)

#         elif data_name and (data_column == "Sr No" or "List No" or "Gender" or "Age" or "Address" or "School"):
#             data_name_lower = data_name.lower()
#             df_column_lower = df[data_column].str.lower()

#             apple_rows = df[df_column_lower == data_name_lower]
#             # apple_rows = pd.read_excel("voter_list_data_1.xlsx")
#             # rows_to_html = apple_rows.to_html()
#             return render_template('print_excel_table.html',  tables =[apple_rows.to_html(classes='data', header="true")])

#         else:
#             error_message = "Please provide both a value and select a column."
#             return render_template('index.html', error_message=error_message)

#     # User accessed the page (GET request)
#     return render_template('index.html', cell1_value="", cell2_value="", cell3_value="")
