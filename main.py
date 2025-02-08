import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date","amount","category","description"]
    
    @classmethod #this decorator means that the function below can access to the class itself but not to it instances
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(cls.COLUMNS)
            df.to_csv(cls.CSV_FILE , index=False)
    @classmethod
    #function to add a new entry to the csv file
    def add_entry(cls , date , amount , category , description):
        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        with open(cls.CSV_FILE,"a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile , fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry Added Successfully")
            
CSV.initialize_csv()