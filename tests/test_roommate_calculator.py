import pytest
import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from roommate_expense_calculator import calculate_totals, calculate_balances, simplify_transactions

def test_calculate_totals():
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack', 'Kate', 'Liam'],
            'Amount': [150, 100, 80, 90, 70, 110, 120, 60, 95, 130, 85, 105]}
    df = pd.DataFrame(data)
    total, share = calculate_totals(df)
    assert total == 1195
    assert share == 1195 / 12

def test_calculate_balances():
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack', 'Kate', 'Liam'],
            'Amount': [150, 100, 80, 90, 70, 110, 120, 60, 95, 130, 85, 105]}
    df = pd.DataFrame(data)
    _, share = calculate_totals(df)
    balances = calculate_balances(df, share)
    assert balances['Alice'] == pytest.approx(150 - share)
    assert balances['Bob'] == pytest.approx(100 - share)
    # Add more assertions for other roommates as needed

def test_simplify_transactions():
    balances = pd.Series({'Alice': 50, 'Bob': -10, 'Charlie': -30, 'David': 40})
    transactions = simplify_transactions(balances)
    assert len(transactions) == 2
    assert "Bob owes Alice" in transactions[0]
    assert "Charlie owes Alice" in transactions[1]  # Updated expected result
