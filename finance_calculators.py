import math

# Ask user to choose 'investment' or 'bond'.
calculation_choice = input("""investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed: """).lower()

# Check if user answered with a valid input and print error message if not.
if calculation_choice != "investment" and calculation_choice != 'bond':
    print("Sorry, thats not a valid input.")

# Else, if user chooses 'investment', ask for deposit amount, interest rate, and how long for.
# Ask for interest type. If user doesnt give a correct answer print an error message.
# Else calculate the interest payed to the user.
elif calculation_choice == "investment":
   deposit = float(input("How much money are you depositing? £"))
   interest_rate = (float(input("What is the percentage interest rate? "))) / 100
   time = float(input("How many years do you want to invest for? "))
   interest_type = input("Do you want 'simple' or 'compounding' interest? ").lower()
   
   if interest_type != "simple" and interest_type != "compounding":
        print("Sorry, thats not a valid input.")
   
   elif interest_type == "simple":
        return_amount = round(deposit * (1 + (interest_rate * time)), 2)
        print(f"You will recieve £{return_amount} after {time} year(s).")
   
   else:
        return_amount = round(deposit * (math.pow(1 + interest_rate), time))
        print(f"You will recieve £{return_amount} after {time} year(s).")

# Else, if user chooses 'bond', ask user for the present value of the property.
# Ask the user for the interest rate percentage and work out monthly interest rate.
# Ask user how many months they will take to repay the loan.
# Calculate the repayment amount and print message for the user.
else:
    present_value = float(input("What is the present value of the house? £"))
    yearly_interest_rate = (float(input("What is the percentage interest rate? "))) / 100
    monthly_interest_rate = yearly_interest_rate / 12
    time = float(input("In how many months would you like to repay the loan? "))
    repayment = round((present_value * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-time)), 2)
    print(f"The monthly repayment amount will be £{repayment}.")