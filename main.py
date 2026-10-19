expenses= []
def save_expense(expense):
  try:
    with open("expenses.txt", "a") as file:
      stringa = f"{expense['description']}|{expense['amount']:.2f}|{expense['category']}"
      file.write(stringa + "\n")
      return True
  except OSError:
      print("Error: could not save the expense.")
      return False

def load_expenses():
  with open("expenses.txt", "r") as file:
    for line in file:
      line= line.strip()
      result= line.split("|")
      expense = {
        "description": result[0],
        "amount": float(result[1]),
        "category": result[2]
      }
      expenses.append(expense)
try:
  load_expenses()
except FileNotFoundError:
  pass

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
  total= sum(expense["amount"] for expense in expenses)
  print(f"Total expenses: €{total:.2f}")

def show_expenses_by_category():
  totals={}
  for expense in expenses:
    category=expense["category"]
    if category not in totals:
      totals[category]=0
    totals[category]+=expense["amount"]
  for category, total in totals.items():
    print(f"{category}: €{total:.2f}")
    
while True: 
  print("\n--- Personal Finance Tracker ---")
  print("1: Add expense")
  print("2: Show expenses")
  print("3: Show total")
  print("4: Show expenses by category")
  print("5: Exit")

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
    print("Goodbye!")
    break
  else:
    print("Invalid option.")
