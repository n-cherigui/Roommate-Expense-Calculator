# Roommate-Expense-Calculator

## Project Overview
Roommate-Expense-Calculator is a Python project designed to help roommates easily split shared expenses. The code takes user input in the form of a CSV file listing all expenses paid by each roommate, and it calculates the amount each person owes or is owed. The goal is to automate the tedious process of balancing expenses, ensuring fairness and transparency in shared living arrangements.

## Methodology
The project uses basic Python programming techniques, including file handling, data parsing, and arithmetic operations. The main algorithm relies on reading expense data from a CSV file, processing the input to determine total expenses, and calculating the fair share of each roommate. 

Key steps:
1. **Data Parsing:** Reads data from a CSV file containing details about expenses (amount, payer, description).
2. **Data Processing:** Aggregates the total expenses paid by each roommate.
3. **Fair Share Calculation:** Computes the average expense per person and determines the balance each roommate owes or is owed.
4. **Optimization:** Ensures minimal transactions between roommates by netting the amounts.

## Data Requirements
The program requires a CSV file input that includes the following columns:
- **Name:** The name of the roommate who paid the expense.
- **Amount:** The amount paid.
- **Description:** A brief description of the expense (e.g., rent, groceries).

Example CSV format:
```csv
Name,Amount,Description
Alice,100,Rent
Bob,50,Groceries
Charlie,30,Utilities
```

## Expected Outcome
The project outputs a summary showing the total amount spent by each roommate, the fair share of expenses, and the exact amount each person owes to others. The program minimizes the number of transactions required to balance the expenses, making it easy for roommates to settle up.

Example output:
```
Total Expenses:
- Alice: $100
- Bob: $50
- Charlie: $30

Fair Share: $60 per person

Balances:
- Alice is owed $40
- Bob owes $10
- Charlie owes $30
```

## Why Use This Project?
Roommate-Expense-Calculator saves time and reduces misunderstandings by automating the calculation of shared expenses. It’s perfect for households, shared apartments, or any living arrangement where costs need to be fairly split among individuals.

Get started by downloading or cloning the repository, providing your CSV file, and running the script to see how much each person owes or is owed.
