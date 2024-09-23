# Roommate-Expense-Calculator
**Name:** Nabil Cherigui
**Student Number:** 5682894

## Project Overview
Roommate-Expense-Calculator is a Python project designed to help roommates easily split shared expenses. The code takes user input in the form of a CSV file listing all expenses paid by each roommate and calculates the amount each person owes or is owed. This tool aims to automate the tedious process of balancing expenses, ensuring fairness and transparency in shared living arrangements.

## Algorithms, Libraries, and Methods
The project utilizes basic Python libraries and methods:
- **Pandas:** For reading, manipulating, and processing CSV data efficiently.
- **Numpy:** For numerical operations, such as calculating sums and averages.
- **Collections (Counter):** For tallying expenses and determining net balances.
- **Algorithm:** The main algorithm involves calculating each roommate's total expenditure, dividing the total evenly among participants, and determining the balance each person owes or is owed to others. It then minimizes the number of transactions required to settle balances between roommates.

## Data Requirements
The program requires a CSV file input with the following columns:
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
The project outputs a summary showing the total amount spent by each roommate, the fair share of expenses, and the exact amount each person owes to others. The program optimizes the settlement process, reducing the number of transactions required.

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
