from storage import load_expenses
from expenses import (
    add_expense,
    show_expenses,
    show_total,
    show_expenses_by_category,
    delete_expense,
    edit_expense,
    search_expenses
)

expenses= []
              
try:
  load_expenses(expenses)
except FileNotFoundError:
  pass
      

while True: 
  print("\n--- Personal Finance Tracker ---")
  print("1: Add expense")
  print("2: Show expenses")
  print("3: Show total")
  print("4: Show expenses by category")
  print("5: Delete expense")
  print("6: Edit expense")
  print("7: Search expense")
  print("8: Exit")

  choice= input("Choose an option: ")

  if choice=="1":
    add_expense(expenses)
  elif choice=="2":
    show_expenses(expenses)
  elif choice=="3":
    show_total(expenses)
  elif choice=="4":
    show_expenses_by_category(expenses)
  elif choice=="5":
    delete_expense(expenses)
  elif choice=="6":
    edit_expense(expenses)
  elif choice=="7":
    search_expenses(expenses)
  elif choice=="8":
    print("Goodbye!")
    break
  else:
    print("Invalid option.")
