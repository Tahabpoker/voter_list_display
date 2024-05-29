import sys
import pandas as pd


df = pd.read_excel("vidhan_sabha/First_Middle_last name.xlsx")
choice = input("[1] Search using name.\n[2] Search using epic number\nEnter your choice: ")
match choice:
    case "1":
        first_name = input("Enter first name: ")
        middle_name = input("Enter middle name: ")
        last_name = input("Enter last name: ")
        if first_name and middle_name and last_name:
            # Search in file
            print(df.loc[(df["First  Name"] == first_name) & (df["Middle Name"] == middle_name) & (df["Last name"] == last_name)].to_string())
        else:
            print("Fields missing")
            sys.exit(1)
    case "2":
        epic_number = input("Enter epic number: ")
        if epic_number:
            # Search
            print(df.loc[df["Epic No"] == epic_number].to_string())
        else:
            print("Epic number missing")
            sys.exit(1)
    case _:
        print("Enter a valid choice")

# print(df.loc[(df["Name"] == " ROSS ") & (df["Age"] == 33)].to_string())
