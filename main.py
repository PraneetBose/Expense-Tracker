import pandas as pd
import matplotlib.pyplot as plt

# Create an empty DataFrame to store expenses
expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

def add_expense():
    date = input("Enter the date (yyyy-mm-dd): ")
    category = input("Enter the expense category: ")
    amount = float(input("Enter the expense amount: $"))
    
    # Append the expense to the DataFrame
    expenses.loc[len(expenses)] = [date, category, amount]

def view_expenses():
    print("Expense Report:")
    print(expenses)

def analyze_expenses():
    # Group expenses by category and calculate total spending in each category
    category_summary = expenses.groupby('Category')['Amount'].sum()
    
    # Plot a pie chart to visualize spending by category
    category_summary.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Expense Distribution by Category')
    plt.show()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Analyze Expenses")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        analyze_expenses()
    elif choice == '4':
        print("Exiting Expense Tracker.")
        break
    else:
        print("Invalid choice. Please try again.")

# You can save the expenses to a CSV file for data persistence
expenses.to_csv('expenses.csv', index=False)
