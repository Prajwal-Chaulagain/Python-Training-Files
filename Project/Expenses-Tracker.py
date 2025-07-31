class ExpenseTracker:
    def __init__(self):
        """Initialize the expense tracker with an empty list of expenses."""
        self.expenses = []

    def display_expenses(self):
        """Displays all recorded expenses grouped by category."""
        if not self.expenses:
            print("\nNo expenses recorded.")
        else:
            print("\nRecorded Expenses:")
            category_totals = {}
            for expense in self.expenses:
                if expense["category"] not in category_totals:
                    category_totals[expense["category"]] = 0
                category_totals[expense["category"]] += expense["amount"]

            for category, total in category_totals.items():
                print(f"{category}: ${total:.2f}")
            print(f"\nTotal Expenses: ${sum(category_totals.values()):.2f}")

    def add_expense(self):
        """Adds a new expense record."""
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: $"))
        self.expenses.append({"category": category, "amount": amount})
        print(
            f"Expense of ${amount} in the category '{category}' recorded successfully!"
        )

    def remove_expense(self):
        """Removes an expense record by index."""
        self.display_expenses()
        try:
            expense_index = int(input("Enter expense number to remove: ")) - 1
            if 0 <= expense_index < len(self.expenses):
                removed_expense = self.expenses.pop(expense_index)
                print(
                    f"Expense of ${removed_expense['amount']} in the category '{removed_expense['category']}' removed successfully!"
                )
            else:
                print("Invalid expense number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to run the expenses tracker."""
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1) Display Expenses")
        print("2) Add Expense")
        print("3) Remove Expense")
        print("4) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.display_expenses()
        elif choice == "2":
            tracker.add_expense()
        elif choice == "3":
            tracker.remove_expense()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()