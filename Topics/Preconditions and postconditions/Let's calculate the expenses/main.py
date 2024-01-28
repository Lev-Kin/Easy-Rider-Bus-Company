import re

string = input()
pattern = r"\$\d+"
expenses = re.findall(pattern, string)
total_expenses = sum(int(expense.strip('$')) for expense in expenses)

print(f"This week you have spent: {total_expenses} dollars")
