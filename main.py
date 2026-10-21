import os
from storage import save_expense, save_all_expenses, load_expenses

expenses= []
              
try:
  load_expenses(expenses)
except FileNotFoundError:
  pass
      
def add_expense():
  description= get_description()
  amount= get_amount()
  category= get_category()
  expense= {
    "description": description,
    "amount": amount,
    "category": category
  }
  if save_expense(expense):
    expenses.append(expense)
    print("Expense added!")
    print(f"Expense added: {expense['description']} - €{expense['amount']:.2f} - {expense['category']}")

def show_expenses():
  if not expenses:
      print("No expenses recorded.")
  else:
      for expense in expenses:
        print (
          f"{expense['description']} - "
          f"€{expense['amount']:.2f} - "
          f"{expense['category']}"
        )

def show_total():
  if not expenses:
    print("No expenses recorded.")
    return
  total= sum(expense["amount"] for expense in expenses)
  print(f"Total expenses: €{total:.2f}")

def show_expenses_by_category():
  if not expenses:
    print("No expenses recorded.")
    return
  totals={}
  for expense in expenses:
    category=expense["category"]
    if category not in totals:
      totals[category]=0
    totals[category]+=expense["amount"]
  for category, total in totals.items():
    print(f"{category}: €{total:.2f}")

def delete_expense():
    if not expenses:
        print("No expenses recorded.")
        return
    counter = 1
    for expense in expenses:
        print(
            f"{counter}: {expense['description']} - "
            f"€{expense['amount']:.2f} - "
            f"{expense['category']}"
        )
        counter += 1
      
    while True:
        indice = input("Quale spesa vuoi eliminare? ")
        try:
            indice = int(indice)
            if indice < 1 or indice > len(expenses):
                print("Indice non valido.")
                continue
            indice -= 1
            break
        except ValueError:
            print("Enter a valid number.")

    removed_expense = expenses.pop(indice)
    if save_all_expenses(expenses):
        print(f"Expense deleted: {removed_expense['description']}")
    else:
        expenses.insert(indice, removed_expense)
        print("Error saving changes.")

def edit_expense():
    if not expenses:
        print("No expenses recorded.")
        return
    counter = 1
    for expense in expenses:
        print(
            f"{counter}: {expense['description']} - "
            f"€{expense['amount']:.2f} - "
            f"{expense['category']}"
        )
        counter += 1
      
    while True:
        indice = input("Quale spesa vuoi modificare? ")
        try:
            indice = int(indice)
            if indice < 1 or indice > len(expenses):
                print("Indice non valido.")
                continue
            indice -= 1
            break
        except ValueError:
            print("Enter a valid number.")
    description= get_description()
    amount= get_amount()
    category= get_category()
    expense= {
        "description": description,
        "amount": amount,
        "category": category
    }
    old_expense = expenses[indice]
    expenses[indice] = expense
    if save_all_expenses(expenses):
        print(f"Expense updated: {expense['description']}")
    else:
        expenses[indice] = old_expense
        print("Error saving changes.")

while True: 
  print("\n--- Personal Finance Tracker ---")
  print("1: Add expense")
  print("2: Show expenses")
  print("3: Show total")
  print("4: Show expenses by category")
  print("5: Delete expense")
  print("6: Edit expense")
  print("7: Exit")

  choice= input("Choose an option: ")

  if choice=="1":
    add_expense()
  elif choice=="2":
    show_expenses()
  elif choice=="3":
    show_total()
  elif choice=="4":
    show_expenses_by_category()
  elif choice=="5":
    delete_expense()
  elif choice=="6":
    edit_expense()
  elif choice=="7":
    print("Goodbye!")
    break
  else:
    print("Invalid option.")
