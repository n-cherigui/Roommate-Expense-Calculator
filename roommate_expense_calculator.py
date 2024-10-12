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

def calculate_balances(expenses_df, share_per_person):
    """Calculate balances (how much each person owes or is owed)."""
    expense_totals = expenses_df.groupby('Name')['Amount'].sum()
    balances = expense_totals - share_per_person
    return balances

def main():
    expenses = read_expenses('expenses.csv')
    total, share = calculate_totals(expenses)
    balances = calculate_balances(expenses, share)
    
    print(f"Balances:\n{balances}")

if __name__ == '__main__':
    main()
