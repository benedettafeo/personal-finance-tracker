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
