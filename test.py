import pandas as pd 

df_152 = pd.read_excel("./static/152.xlsx")

vidhan_Sabha = "152"

data_name = "XWC1569359"
data_column = "Epic No"


def search(data_name, data_column, df):
    data_name_lower = data_name.lower()
    df_column_lower = df[data_column].str.lower()

    apple_rows = df[df_column_lower == data_name_lower]
    return apple_rows


match vidhan_Sabha:
    case "152": 
        print(search(data_name, data_column, df_152))
        

