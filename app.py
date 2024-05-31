# app.py
import pandas as pd  # type: ignore
from flask import Flask, render_template, request, send_file, url_for # type: ignore

# Read the Excel file into a data frame
df = pd.read_excel('vidhan_sabha/test_voter.xlsx')
df1 = pd.read_excel('data.xlsx')


#create a function to search by epic_no in the excel using pandas


def search_by_name(first_name, middle_name1, last_name, df, new_data, df1):
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

        save_phone_number_in_excel(new_data=new_data, df1=df1)


        return render_template("modal.html", cell1_value=cell1_value, cell2_value=cell2_value, cell3_value=cell3_value, cell4_value=cell4_value, cell5_value=cell5_value, cell6_value=cell6_value, cell7_value=cell7_value, cell8_value=cell8_value)
    else :
        error_message = "Value '{}' '{}' '{}' not found in the data PLEASE ENTER VALID NAME!!!".format(first_name, middle_name1, last_name)
        return render_template('index.html', error_message=error_message)

def save_phone_number_in_excel(new_data, df1):
    df1 = df1._append(new_data, ignore_index=True)
    df1.to_excel('data.xlsx', index=False)



# Flask constructor
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        
        # user submitted form
        first_name = request.form.get("first_name").upper()
        middle_name = request.form.get("middle_name").upper()
        last_name = request.form.get("last_name").upper()
        phone_number = request.form.get("phone_number")
        epic_no = "test"

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

# Append the new data to the DataFrame
        if phone_number:
            if not first_name and not middle_name and not last_name :
                print("we have been here in if 1")
                if  epic_no :
                    print("we have been here in if 2")

                else :
                    error_message = "Enter Either Your Full name or your Epic Number"
                    return render_template('index.html', error_message=error_message)
                    

            else :
                print("we have been here in else 2 ")
                return search_by_name(first_name=first_name, middle_name1=middle_name, last_name=last_name, df=df,new_data = new_data_with_name,df1=df1) 
        else : 
            error_message = "enter Phone Number"
            return render_template("index.html",error_message = error_message)
        
    return render_template("index.html")

@app.route("/10opt3hhh")
def display_excel():
    df = pd.read_excel("data.xlsx")
    return render_template("10opt3hhh.html", tables=[df.to_html(classes='data', header="true")])




@app.route("/download_excel")
def download_excel():
    # Read the Excel file
    df = "data.xlsx"
    return send_file(df, as_attachment = True)


if __name__ == "__main__":
    app.run(debug=True)

    # , host="0.0.0.0"
    
