import pandas as pd

def read_expenses(file_path):
    """Read expenses from CSV file using Pandas."""
    return pd.read_csv(file_path)

def calculate_totals(expenses_df):
    """Calculate total expenses per person and the fair share."""
    total_expense = expenses_df['Amount'].sum()
    num_roommates = expenses_df['Name'].nunique()
    share_per_person = total_expense / num_roommates
    return total_expense, share_per_person

def main():
    expenses = read_expenses('expenses.csv')
    total, share = calculate_totals(expenses)
    print(f"Total expenses: ${total:.2f}")
    print(f"Each roommate should pay: ${share:.2f}")

if __name__ == '__main__':
    main()
