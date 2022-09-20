expense = [2200, 2350, 2600, 2130, 2190]

expense_spent = expense[1] - expense[0]

print(f"\n1. In Feb, you spent {expense_spent} compared to January")

total_expense = sum(expense[:2])
print(f"\n2. The total expense in first quarter is {total_expense}")

# Using Linear Search
var = 2000 in expense
print("\n", var)




