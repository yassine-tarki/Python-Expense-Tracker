expenses = []


def add_expense():
    description = input("Description: ")
    amount = float(input("Amount: "))
    expenses.append({
        "description": description,
        "amount": amount
    })
    print("Expense added!")


def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - "
              f"{expense['amount']:.2f}")


def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total: {total:.2f}")

def delete_expense():
    if not expenses:
        print("No expenses recorded.")
        return
    show_expenses()
    try:
        index = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= index < len(expenses):
            deleted_expense = expenses.pop(index)
            print(f"Deleted expense: {deleted_expense['description']} - "
                  f"{deleted_expense['amount']:.2f}")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")
def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Delete an expense")
        print("4. Show total")
        print("3. Show total")
        print("4. Exit")
        choice = input("Your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
