from storage import save_expense, save_all_expenses


def get_amount ():
  while True:
    amount = input("Amount (€): ")
    try:
      amount = float(amount)
      if amount>0: 
        return amount
      else:
        print("Amount must be greater than 0.")
    except ValueError:
      print("Enter a valid number.")

def get_description():
  while True:
    description = input("Description: ").strip()
    if description:
      return description
    else:
      print("Description cannot be empty.")

def get_category():
  while True:
    category = input("Category: ").strip()
    if category:
      return category.capitalize()
    else:
      print("Category cannot be empty.")

def add_expense(expenses):
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

def show_expenses(expenses):
  if not expenses:
      print("No expenses recorded.")
  else:
      for expense in expenses:
        print (
          f"{expense['description']} - "
          f"€{expense['amount']:.2f} - "
          f"{expense['category']}"
        )

def show_total(expenses):
  if not expenses:
    print("No expenses recorded.")
    return
  total= sum(expense["amount"] for expense in expenses)
  print(f"Total expenses: €{total:.2f}")

def show_expenses_by_category(expenses):
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

def delete_expense(expenses):
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

def edit_expense(expenses):
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

def search_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    found= False
    search = input("Search: ").strip().lower()
    for expense in expenses:
      if search in expense["description"].lower():
        found= True
        print (
          f"{expense['description']} - "
          f"€{expense['amount']:.2f} - "
          f"{expense['category']}"
        )
    if not found:
      print("No expenses found.")
