import os

def save_expense(expense):
  try:
    with open("expenses.txt", "a") as file:
      stringa = f"{expense['description']}|{expense['amount']:.2f}|{expense['category']}"
      file.write(stringa + "\n")
      return True
  except OSError:
      print("Error: could not save the expense.")
      return False

def save_all_expenses(expenses):
  try:
    with open("expenses.tmp", "w") as file:
      for expense in expenses:
        stringa = f"{expense['description']}|{expense['amount']:.2f}|{expense['category']}"
        file.write(stringa + "\n")
  except OSError:
      print("Error: could not save the expense.")
      return False
  try:
      os.replace("expenses.tmp", "expenses.txt")
      return True
  except OSError:
      print("Error: could not replace the file.")
      try:
          os.remove("expenses.tmp")
      except OSError:
          pass
      return False

def load_expenses(expenses):
    with open("expenses.txt", "r") as file:
        for line in file:
            line = line.strip()
            try:
                result = line.split("|")
                if len(result) != 3 or not result[0].strip() or not result[2].strip():
                    print("Warning: skipping an invalid expense.")
                    continue
                expense = {
                    "description": result[0].strip(),
                    "amount": float(result[1]),
                    "category": result[2].strip()
                }
                if expense["amount"] <= 0:
                    print("Warning: skipping an invalid expense.")
                    continue
                expenses.append(expense)
            except (ValueError, IndexError):
                print("Warning: skipping an invalid expense.")
