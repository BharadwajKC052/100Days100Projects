print("Welcome to SplitWise and lets split our latest Spends")

# Get the total bill amount

total_bill = float(input("Enter the total bill amount in ₹: "))
howManySplits = int(input("How many people to split the bill: "))
tipCheck = str(input("Do you want to give tip Y/N: "))
if tipCheck == "Y":
    tipPercent = float(input("how much do you want to give tip in %: "))
    tipAmount = (tipPercent/100) * total_bill
    total_bill += tipAmount
    perpersonCheck = total_bill /howManySplits
    print("Each person Should pay ₹ :{}".format(perpersonCheck) )
else:
    perpersonCheck = total_bill /howManySplits
    print("Each person Should pay ₹ :{}".format(perpersonCheck) )

    

