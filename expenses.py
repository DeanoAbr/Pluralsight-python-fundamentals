total = 0

expenses = []

num_expenses = int(input("How many expenses would you like to capture? "))

for i in range(num_expenses):
    expenses.append(float(input("Please enter an expense: ")))

total = sum(expenses)

print("You have spent: R" + str(total))