expense = [2200, 2350, 2600, 2130, 2190]

expense_spent = expense[1] - expense[0]

print(f"\n1. In Feb, you spent {expense_spent} compared to January")

total_expense = sum(expense[:2])
print(f"\n2. The total expense in first quarter is {total_expense}")

# Using Linear Search
var = 2000 in expense
print("\n", var)

expense.insert(4, 1980)

expense[3] - 200
print(expense)

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

length_heros = len(heros)
print(f"\nThe length of heros is {length_heros}")

heros.insert(5, "black panther")
print("\n", heros)

del heros[5]
print(heros)

max = int(input("Enter a max number: "))

odd_number = []

for i in range(1, max):
    if i % 2 == 1:
        odd_number.append(i)
print("Odd number is ", max)










