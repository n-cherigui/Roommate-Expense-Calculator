import pandas as pd
import csv

def read_expenses(file_path):
    """
    Read expenses from a CSV file using Pandas.

    Args:
        file_path (str): The path to the CSV file containing expenses.

    Returns:
        DataFrame: A Pandas DataFrame containing the expense data.
    """
    return pd.read_csv(file_path)

def calculate_totals(expenses_df):
    """
    Calculate the total expenses and the fair share per person.

    Args:
        expenses_df (DataFrame): DataFrame containing roommates' expenses.

    Returns:
        float: The total amount of expenses.
        float: The amount each person should contribute.
    """
    total_expense = expenses_df['Amount'].sum()
    num_roommates = expenses_df['Name'].nunique()
    share_per_person = total_expense / num_roommates
    return total_expense, share_per_person

def calculate_balances(expenses_df, share_per_person):
    """
    Calculate how much each person owes or is owed based on their expenses.

    Args:
        expenses_df (DataFrame): DataFrame containing expenses data.
        share_per_person (float): The amount each person should contribute.

    Returns:
        Series: A Pandas Series containing the balance for each person.
    """
    expense_totals = expenses_df.groupby('Name')['Amount'].sum()
    balances = expense_totals - share_per_person
    return balances

def simplify_transactions(balances):
    """
    Minimize the number of transactions required to settle balances.

    Args:
        balances (Series): A Pandas Series containing balances for each person.

    Returns:
        list: A list of strings indicating the transactions required to settle balances.
    """
    owed = balances[balances < 0]
    owed_to = balances[balances > 0]
    transactions = []
    
    for debtor, debt in owed.items():
        for creditor, credit in owed_to.items():
            if debt == 0:
                break
            payment = min(-debt, credit)
            transactions.append(f"{debtor} owes {creditor} ${payment:.2f}")
            debt += payment
            credit -= payment
            owed_to[creditor] = credit
        owed[debtor] = debt
    return transactions

def write_to_csv(balances, transactions, file_name='output.csv'):
    """
    Write the balances and transactions to a CSV file.

    Args:
        balances (Series): A Pandas Series containing the final balances for each person.
        transactions (list): A list of strings detailing the transactions required to settle balances.
        file_name (str): The name of the output CSV file.

    Returns:
        None
    """
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Writing the balances
        writer.writerow(["Name", "Balance"])
        for name, balance in balances.items():
            writer.writerow([name, round(balance, 2)])
        
        # Writing the transactions
        writer.writerow([])
        writer.writerow(["Transactions"])
        for transaction in transactions:
            writer.writerow([transaction])

def main():
    """
    Main function to read expenses, calculate totals and balances, and write results to a CSV file.

    The function reads expenses from a CSV file, calculates total expenses and each person's share, computes the balances, and then simplifies the transactions required to settle the balances.
    The output is saved to an 'output.csv' file.
    """
    expenses = read_expenses('expenses.csv')
    total, share = calculate_totals(expenses)
    balances = calculate_balances(expenses, share)
    transactions = simplify_transactions(balances)

    # Save the output to CSV
    write_to_csv(balances, transactions)
    print("Output saved to 'output.csv'")

if __name__ == '__main__':
    main()
