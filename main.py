expenses = []
budget = 0


def add_expense():
    print("\n--- Add Expense ---")

    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date: ")

    expenses.append([amount, category, date])

    print("Expense added successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        for i in range(len(expenses)):
            print(i + 1, ".", 
                  "₹", expenses[i][0],
                  "|", expenses[i][1],
                  "|", expenses[i][2])


def analyse_expenses():
    print("\n--- Expense Analysis ---")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    total = 0
    highest = expenses[0][0]
    lowest = expenses[0][0]

    for expense in expenses:
        total = total + expense[0]

        if expense[0] > highest:
            highest = expense[0]

        if expense[0] < lowest:
            lowest = expense[0]

    average = total / len(expenses)

    print("Total Expense: ₹", total)
    print("Average Expense: ₹", average)
    print("Highest Expense: ₹", highest)
    print("Lowest Expense: ₹", lowest)


def search_expense():
    print("\n--- Search Expense ---")

    search = input("Enter category: ")

    found = False

    for expense in expenses:
        if expense[1].lower() == search.lower():
            print("₹", expense[0],
                  "|", expense[1],
                  "|", expense[2],
                  "|", expense[3])
            found = True

    if found == False:
        print("No expense found.")


def set_budget():
    global budget

    budget = float(input("Enter your budget: "))

    print("Budget set to ₹", budget)


def budget_status():
    if budget == 0:
        print("Budget has not been set.")
        return

    total = 0

    for expense in expenses:
        total = total + expense[0]

    remaining = budget - total

    print("\n--- Budget Status ---")
    print("Budget: ₹", budget)
    print("Total Spent: ₹", total)

    if remaining > 0:
        print("Remaining Budget: ₹", remaining)

    elif remaining == 0:
        print("You have used your full budget.")

    else:
        print("Budget exceeded by ₹", -remaining)


# Main Program

while True:

    print("\n==============================")
    print("    PERSONAL EXPENSE TRACKER")
    print("==============================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Analyse Expenses")
    print("4. Search Expense")
    print("5. Set Budget")
    print("6. Budget Status")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        analyse_expenses()

    elif choice == "4":
        search_expense()

    elif choice == "5":
        set_budget()

    elif choice == "6":
        budget_status()

    elif choice == "7":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice.")