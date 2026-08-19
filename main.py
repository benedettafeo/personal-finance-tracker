expenses= []

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
    print("Expense added!")
    
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
