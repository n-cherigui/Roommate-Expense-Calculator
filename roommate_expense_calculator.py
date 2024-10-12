import pandas as pd

def read_expenses(file_path):
    """Read expenses from CSV file using Pandas."""
    return pd.read_csv(file_path)

def main():
    file_path = 'expenses.csv'
    expenses = read_expenses(file_path)
    print(expenses)

if __name__ == '__main__':
    main()
