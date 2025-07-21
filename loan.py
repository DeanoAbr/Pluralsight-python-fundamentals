# Get details of loan

money_owed = float(input("How much money do you owe?\n"))  #R500,000

interest_rate = float(input("What is the interest rate of the loan?\n"))  #12%

payment = float(input("What will your monthly payment be?\n"))  #R7,500

months = int(input("How many months do you want to see the result for?\n"))  #24


monthly_rate = interest_rate/100/12

for i in range(months):

    # Calculate interest to pay

    interest_paid = money_owed*monthly_rate

    #add in interest

    money_owed = money_owed+interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in ", i+1, "months")
        break

    #make payment
    money_owed = money_owed-payment

    print("Paid ", payment, "of which ", interest_paid, "was interest. ", end= " ")
    print("Now I owe ", money_owed)