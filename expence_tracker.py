from expense import Expense
import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Expense Tracker")
    expense_file_path = "expenses.csv"
    budget = 2000
    expense = get_user_expense()
    print(expense)
    save_expense(expense, expense_file_path)
    summarize_expense(expense_file_path, budget)
    expense_analysis(expense_file_path)
    pass

def get_user_expense():
    print("Getting user expenses")
    expense_name = input("Enter expense name:")
    expense_amt = float(input("Enter expense amount:"))
    expense_catg = [
        "Food",
        "Home",
        "Fun",
        "Work",
        "Miscallaneous"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_catg):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_catg)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_catg)):
            selected_category = expense_catg[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amt
            )
            return new_expense
        else:
            print("Invalid category. Please try again!")

def save_expense(expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(expense_file_path, budget):
    print("Summarizing user expenses")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amt, expense_catg = line.strip().split(",")
            line_expense = Expense(
                name = expense_name, amount = float(expense_amt), category=expense_catg
            )
            print(line_expense)
            expenses.append(line_expense)
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expense By Categories:")
    for key, amount in amount_by_category.items():
        print(f" {key}: Rs.{amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent Rs.{total_spent:.2f} this month!")

    remaining_budget = budget - total_spent

    print(green("INSIGHTS"))
    if remaining_budget > 0:
        print("You're under budget! Great job!")
    elif remaining_budget == 0:
        print("You've exactly spent your budget. Keep an eye on your expenses.")
    else:
        print("You've exceeded your budget. Consider adjusting your expenses.")

    print(green(f"Budget Remaining: Rs.{remaining_budget:.2f}"))

def expense_analysis(expense_file_path):

    df = pd.read_csv(expense_file_path)
    x = df['Miscallaneous']
    y = df['0.0']

    plt.figure(figsize=(10, 6))
    plt.title("Spending trends")
    plt.xlabel('Expense category')
    plt.ylabel('Total Amount')
    plt.plot(x, y)
    plt.show()

def green(text):
    return f"\033[92m{text}\033[0m"

if _name_ == "_main_":
    main()
