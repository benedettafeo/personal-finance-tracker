expenses= []
def save_expense(expense):
  with open("expenses.txt", "a") as file:
      stringa = f"{expense['description']}|{expense['amount']:.2f}|{expense['category']}"
      file.write(stringa + "\n")

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

while True: 
  print("\n--- Personal Finance Tracker ---")
  print("1: Add expence")
  print("2: Show expenses")
  print("3: Show total")
  print("4: Exit")

  choice= input("Choose an option: ")

  if choice=="1":
    description= input("Description: ")
    amount= float(input("Amount (€): ")
    category= input("category: ")

    expense= {
      "description": description,
      "amount": amount,
      "category": category
    }
    expenses.append(expense)
    save expense(expense)
    print("Expense added!")
    print(f”Expense added: {expense[‘description’]} - €{expense[‘amount’]:.2f} - {expense[‘category’]}”)
    
  elif choice=="2":
    if not expenses:
      print("No expenses recorded.")
    else:
      for expense in expenses:
        print (
          f"{expense['description']} - "
          f"€{expense['amount']:.2f} - "
          f"{expense['category']}"
        )
  elif choice=="3":
    total= sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: €{total:.2f}")
  elif choice=="4":
    print("Goodbye!")
    break
  else:
    print("Invalid option.")
