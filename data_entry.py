#the purpose of this file is to write all functions and logic related to input from user
from datetime import datetime

date_format = "%d-%m-%Y"

CATEGORIES = {'I': 'Income' , 'E': 'Expense'}


def get_date(prompt , read_default_date=False):
    str_date = input(prompt)

    if read_default_date and not str_date:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(str_date , date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid Date Format ! Please enter a valid date with the following format: dd-mm-yyyy")
        return get_date(prompt , read_default_date)


def get_amount():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be non-negative non-zero value !")
        return amount
    except ValueError as ve:
        print(ve)
        return get_amount()


def get_category():
    category = input("Enter category , 'I' for Income and 'E' for Expense: ")
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("Please enter a valid category ! ('I' or 'E')")
    return get_category()
    

def get_description():
    description = input("Enter description (optional) : ")