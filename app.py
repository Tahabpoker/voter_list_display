# app.py
import pandas as pd  # type: ignore
from flask import Flask, render_template, request  # type: ignore


def search(data_name, data_column, df):
    data_name_lower = data_name.lower()
    df_column_lower = df[data_column].str.lower()

    apple_rows = None
    apple_rows = df[df_column_lower == data_name_lower]
    return apple_rows


# Read the Excel file into a data frame
df_153 = pd.read_excel("./vidhan_sabha/153.xlsx")
df_154 = pd.read_excel("./vidhan_sabha/154.xlsx")
df_152 = pd.read_excel("./vidhan_sabha/152.xlsx")
df_155 = pd.read_excel("./vidhan_sabha/155.xlsx")
df_156 = pd.read_excel("./vidhan_sabha/156.xlsx")
df_157 = pd.read_excel("./vidhan_sabha/157.xlsx")
df_158 = pd.read_excel("./vidhan_sabha/158.xlsx")
df_159 = pd.read_excel("./vidhan_sabha/159.xlsx")
df_160 = pd.read_excel("./vidhan_sabha/160.xlsx")
df_161 = pd.read_excel("./vidhan_sabha/161.xlsx")
df_162 = pd.read_excel("./vidhan_sabha/162.xlsx")
df_163 = pd.read_excel("./vidhan_sabha/163.xlsx")
df_164 = pd.read_excel("./vidhan_sabha/164.xlsx")
df_165 = pd.read_excel("./vidhan_sabha/165.xlsx")
df_166 = pd.read_excel("./vidhan_sabha/166.xlsx")
df_167 = pd.read_excel("./vidhan_sabha/167.xlsx")
df_168 = pd.read_excel("./vidhan_sabha/168.xlsx")
df_169 = pd.read_excel("./vidhan_sabha/169.xlsx")
df_170 = pd.read_excel("./vidhan_sabha/170.xlsx")
df_171 = pd.read_excel("./vidhan_sabha/171.xlsx")
df_172 = pd.read_excel("./vidhan_sabha/172.xlsx")
df_173 = pd.read_excel("./vidhan_sabha/173.xlsx")
df_174 = pd.read_excel("./vidhan_sabha/174.xlsx")
df_175 = pd.read_excel("./vidhan_sabha/175.xlsx")
df_176 = pd.read_excel("./vidhan_sabha/176.xlsx")
df_177 = pd.read_excel("./vidhan_sabha/177.xlsx")
df_178 = pd.read_excel("./vidhan_sabha/178.xlsx")
df_179 = pd.read_excel("./vidhan_sabha/179.xlsx")
df_180 = pd.read_excel("./vidhan_sabha/180.xlsx")
df_181 = pd.read_excel("./vidhan_sabha/181.xlsx")
df_182 = pd.read_excel("./vidhan_sabha/182.xlsx")
df_183 = pd.read_excel("./vidhan_sabha/183.xlsx")
df_184 = pd.read_excel("./vidhan_sabha/184.xlsx")
df_185 = pd.read_excel("./vidhan_sabha/185.xlsx")
df_186 = pd.read_excel("./vidhan_sabha/186.xlsx")
df_187 = pd.read_excel("./vidhan_sabha/187.xlsx")


# Flask constructor
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # user submitted form
        data_name = request.form.get("data_name")
        data_column = request.form.get("data_column")
        vidhan_Sabha = request.form.get("vidhan_Sabha")

        if data_name and data_column != "None":


            match vidhan_Sabha:
                case "152":
                    tables = search(data_name, data_column,df_152)
                case "153":
                    tables = search(data_name, data_column, df_153)
                case "154":
                    tables = search(data_name, data_column, df_154)
                case "155":
                    tables = search(data_name, data_column, df_155)
                case "156":
                    tables = search(data_name, data_column, df_156)
                case "157":
                    tables = search(data_name, data_column, df_157)
                case "158":
                    tables = search(data_name, data_column, df_158)
                case "159":
                    tables = search(data_name, data_column, df_159)
                case "160":
                    tables = search(data_name, data_column, df_160)
                case "161":
                    tables = search(data_name, data_column, df_161)
                case "162":
                    tables = search(data_name, data_column, df_162)
                case "163":
                    tables = search(data_name, data_column, df_163)
                case "164":
                    tables = search(data_name, data_column, df_164)
                case "165":
                    tables = search(data_name, data_column, df_165)
                case "166":
                    tables = search(data_name, data_column, df_166)
                case "167":
                    tables = search(data_name, data_column, df_167)
                case "168":
                    tables = search(data_name, data_column, df_168)
                case "169":
                    tables = search(data_name, data_column, df_169)
                case "170":
                    tables = search(data_name, data_column, df_170)
                case "171":
                    tables = search(data_name, data_column, df_171)
                case "172":
                    tables = search(data_name, data_column, df_172)
                case "173":
                    tables = search(data_name, data_column, df_173)
                case "174":
                    tables = search(data_name, data_column, df_174)
                case "175":
                    tables = search(data_name, data_column, df_175)
                case "176":
                    tables = search(data_name, data_column, df_176)
                case "177":
                    tables = search(data_name, data_column, df_177)
                case "178":
                    tables = search(data_name, data_column, df_178)
                case "179":
                    tables = search(data_name, data_column, df_179)
                case "180":
                    tables = search(data_name, data_column, df_180)
                case "181":
                    tables = search(data_name, data_column, df_181)
                case "182":
                    tables = search(data_name, data_column, df_182)
                case "183":
                    tables = search(data_name, data_column, df_183)
                case "184":
                    tables = search(data_name, data_column, df_184)
                case "185":
                    tables = search(data_name, data_column, df_185)
                case "186":
                    tables = search(data_name, data_column, df_186)
                case "187":
                    tables = search(data_name, data_column, df_187)

            if not len(tables): # \
                error_message = "Value '{}' not found in the specified column '{}'".format(data_name, data_column)
                return render_template("index.html", error_message = error_message)

            return render_template("index.html", tables = [tables.to_html(classes='data', header="true")])
        
        else:
            error_message = "Please provide both a value and select a column."
            return render_template('index.html', error_message=error_message)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

    # , host="0.0.0.0"
    


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
                # error_message = "Value '{}' not found in the specified column '{}'".format(data_name, data_column)
                # return render_template('index.html', error_message=error_message)

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
