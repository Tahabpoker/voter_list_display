# app.py
import pandas as pd  # type: ignore
from flask import Flask, render_template, request  # type: ignore

# Read the Excel file into a data frame
df = pd.read_excel('vidhan_sabha/test_voter.xlsx')
df1 = pd.read_excel('data.xlsx')

print(df)
#create a function to search by epic_no in the excel using pandas
def search_by_epic_no(epic_number, df):
    if epic_number:
        # Search
        df_1 = df.loc[df["epic_no"] == epic_number]
        if not df_1.empty:
            # Extract the first row as a Series (single row)
            first_row_data = df_1.iloc[0]

            cell1_value = first_row_data['first_name']#
            cell2_value = first_row_data['middle_name']#
            cell3_value = first_row_data['last_name']#
            cell4_value = first_row_data['school']#
            cell5_value = first_row_data['age']#
            cell6_value = first_row_data['epic_no']#
            cell7_value = first_row_data['booth_number']#
            cell8_value = first_row_data['address']#
            
            print(f"Name: {cell1_value} {cell2_value} {cell3_value}\nSchool: {cell4_value}\nAge: {cell5_value}\nEpic No: {cell6_value}\nBooth No: {cell7_value}\nAddress: {cell8_value}")

            return render_template("modal.html", cell1_value=cell1_value, cell2_value=cell2_value, cell3_value=cell3_value, cell4_value=cell4_value, cell5_value=cell5_value, cell6_value=cell6_value, cell7_value=cell7_value, cell8_value=cell8_value)
        else :
            error_message = "Value '{}' not found in the data PLEASE ENTER VALID EPIC NUMBER!!!".format(epic_number)
            return render_template('index.html', error_message=error_message)


    return render_template('index.html') 
    

def search_by_name(first_name, middle_name1, last_name, df):
    df_1 = df.loc[(df["first_name"] == first_name) & (df['middle_name'] == middle_name1) & (df["last_name"] == last_name)]
    if not df_1.empty:
        # Extract the first row as a Series (single row)
        first_row_data = df_1.iloc[0]

        cell1_value = first_row_data['first_name']#
        cell2_value = first_row_data['middle_name']#
        cell3_value = first_row_data['last_name']#
        cell4_value = first_row_data['school']#
        cell5_value = first_row_data['age']#
        cell6_value = first_row_data['epic_no']#
        cell7_value = first_row_data['booth_number']#
        cell8_value = first_row_data['address']#
        
        print(f"Name: {cell1_value} {cell2_value} {cell3_value}\nSchool: {cell4_value}\nAge: {cell5_value}\nEpic No: {cell6_value}\nBooth No: {cell7_value}\nAddress: {cell8_value}")

        return render_template("modal.html", cell1_value=cell1_value, cell2_value=cell2_value, cell3_value=cell3_value, cell4_value=cell4_value, cell5_value=cell5_value, cell6_value=cell6_value, cell7_value=cell7_value, cell8_value=cell8_value)
    else :
        error_message = "Value '{}' '{}' '{}' not found in the data PLEASE ENTER VALID NAME!!!".format(first_name, middle_name1, last_name)
        return render_template('index.html', error_message=error_message)

def save_phone_number_in_excel(new_data, df):
    df = df._append(new_data, ignore_index=True)
    df.to_excel('data.xlsx', index=False)



# Flask constructor
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        
        # user submitted form
        first_name = request.form.get("first_name").upper()
        middle_name = request.form.get("middle_name").upper()
        last_name = request.form.get("last_name").upper()
        epic_no = request.form.get("epic_no").upper()
        phone_number = request.form.get("phone_number")


        print(first_name)
        print(middle_name)
        print(last_name)
        print(epic_no)
        print(phone_number)

        new_data_with_name = {
            'first_name': first_name,
            'mddle_name': middle_name,
            'last_name': last_name,
            'phone_number' : phone_number
        }
        new_data_without_name = {
            'first_name': epic_no,
            'mddle_name': "none",
            'last_name': "none",
            'phone_number' : phone_number
        }

# Append the new data to the DataFrame
        if phone_number:
            if not first_name and not middle_name and not last_name :
                print("we have been here in if 1")
                if not epic_no :
                    print("we have been here in if 2")

                    error_message = "Enter Either Your Full name or your Epic Number"
                    return render_template('index.html', error_message=error_message)
                    
                else :
                    print("we have been here in else 1 ")
                    save_phone_number_in_excel(new_data=new_data_without_name, df = df1)
                    return search_by_epic_no(epic_number=epic_no, df=df)
                    

            else :
                print("we have been here in else 2 ")
                save_phone_number_in_excel(new_data=new_data_with_name, df = df1) 
                return search_by_name(first_name=first_name, middle_name1=middle_name, last_name=last_name, df=df) 
        else : 
            error_message = "enter Phone Number"
            return render_template("index.html",error_message = error_message)
        
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
