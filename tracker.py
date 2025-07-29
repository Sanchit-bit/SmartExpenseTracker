import csv
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

file_name = "expenses.csv"

# 🔄 Initialize CSV file if not exists
if not os.path.exists(file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Amount", "Note"])

def add_expense():
    date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (Food/Transport/Shopping/Other): ")
    amount = float(input("Enter amount: ₹"))
    note = input("Optional note: ")

    with open(file_name, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])
    print("✅ Expense added successfully!")

def show_expenses():
    df = pd.read_csv(file_name)
    print("\n📊 All Expenses:")
    print(df.tail(10))  # last 10 rows

def monthly_summary():
    month = input("Enter month (e.g. 2025-06): ")
    df = pd.read_csv(file_name)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')

    filtered = df[df['Month'] == month]
    if filtered.empty:
        print("⚠️ No data for that month.")
        return

    print(f"\nSummary for {month}:")
    print(filtered.groupby("Category")["Amount"].sum())

    # Pie chart
    filtered.groupby("Category")["Amount"].sum().plot.pie(autopct="%1.1f%%", figsize=(6,6))
    plt.title(f"Expense Breakdown - {month}")
    plt.show()

def menu():
    while True:
        print("\n====== Smart Expense Tracker ======")
        print("1. Add Expense")
        print("2. Show Recent Expenses")
        print("3. Monthly Summary (with chart)")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    menu()
