#the purpose of this file is to write all functions and logic related to input from user
from datetime import datetime

date_format = "%d-%m-%Y"

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
    pass

def get_category():
    pass

def get_description():
    pass
