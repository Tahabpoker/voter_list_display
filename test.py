import pandas as pd 

df_152 = pd.read_excel("./static/152.xlsx")

vidhan_Sabha = "152"

data_name = "XWC1569359"
data_column = "Epic No"


def search(data_name, data_column, df):
    data_name_lower = data_name.lower()
    df_column_lower = df[data_column]
    print(df_column_lower)

    apple_rows = df[df_column_lower == data_name_lower]
    return apple_rows


# list_numbers = [str(i) for i in range(152, 188)]
# if vidhan_Sabha in list_numbers:
#     print(search(data_name, data_column, "df_{}.".format(vidhan_Sabha)))

# match vidhan_Sabha:
#     case "152": 
#         tables = search(data_name, data_column, df_152)
#         if not len(tables):
#             print("empty")
#         else:
#             print("full")

# data_columns = ["Epic No", "Sr No", "School"]

# print(df_152[data_column].str.lower() == data_name.lower())
print(search(data_name, data_column, df_152))

'''
'''

