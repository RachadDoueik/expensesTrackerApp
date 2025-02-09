import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount , get_category , get_date , get_description
import matplotlib.pyplot as plt


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date","amount","category","description"]
    FORMAT = "%d-%m-%Y"
    
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
    #function to get all transactions within a date range
    @classmethod
    def get_transactions_in_range(cls , start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"] , format=CSV.FORMAT)
        startdate = datetime.strptime(start_date , CSV.FORMAT)
        enddate = datetime.strptime(end_date , CSV.FORMAT)
        mask = (df["date"] >= startdate) & (df["date"] <= enddate)
        trans_in_range_df = df.loc[mask]
        if trans_in_range_df.empty:
            print("No transactions are made in this date range !")
        else:
            print(f"Transactions made from {startdate.strftime(format=CSV.FORMAT)} to {enddate.strftime(format=CSV.FORMAT)}: ")
            print(
                trans_in_range_df.to_string(
                    index=False , formatters={"date": lambda x: x.strftime(format=CSV.FORMAT)}
                ))
            total_income = trans_in_range_df[trans_in_range_df["category"] == "Income"]["amount"].sum()
            total_expense = trans_in_range_df[trans_in_range_df["category"] == "Expense"]["amount"].sum()
            print("\n")
            print("Summary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")
        return trans_in_range_df
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or Press Enter for 'Today Date': ")
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date , amount , category , description)

def plot_transactions(df):
    df.set_index('date' , inplace=True)
    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index , fill_value = 0)
    expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index , fill_value = 0)
    plt.figure(figsize=(10,5))
    plt.plot(income_df.index , income_df["amount"] ,label="Income",color="g")
    plt.plot(expense_df.index , expense_df["amount"] ,label="Expense",color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense over time")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("\nPlease choose an operation:")
        print("1. Add Transaction")
        print("2. Show Transactions")
        print("3. Exit")
        choice = input("You Choice: ")
        choice = int(choice)
        if choice == 1:
            add()
        elif choice == 2:
            start_date = input("Enter start date (dd-mm-yyyy): ")
            end_date = input("Enter end date (dd-mm-yyyy): ")
            df = CSV.get_transactions_in_range(start_date , end_date)
            visualize = input("Do you want to visualize your data ? (y/n): ")
            if visualize.lower() == 'y':
                plot_transactions(df)
        elif choice == 3:
            print("Leaving...")
            break
        else:
            print("Invalid input error !")


if __name__ == "__main__":
    main()