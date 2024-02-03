#calculate the interest on investment
#calculate interest on home loan
#ask user input if they want to calculate investment or bond
#Make sure input is not case sensitive
#if investment is chosen, ask for principal, rate, time input and if simple or compound
#if bond is chosen, ask for present value, number of months for repayment and interest rate
import math

while True:
    user_selection = "investment - to calculate the amount of interest you'll earn on your investment\n"
    user_selection += "bond - to calculate the amount you'll have to pay on a home loan\n\n"
    user_selection += "Enter either 'investment' or 'bond' from the menu above to proceed: "

    selection = input(user_selection)
    selection = selection.lower()
    selection = selection.strip()


    if (selection == "investment"):
        principal = float(input("Please enter the amount you are depositing: "))                                                                            
        rate = float(input("Please enter interest rate in percentage: "))         
        rate = float(rate) / 100
        time = float(input("Please enter number of years you plan on investing: "))
        interest = input("Do you want simple or compound?")
        interest = interest.lower()
        interest = interest.strip()
      
        if interest == "simple":
            calculate_simple_investment = principal*(1 + rate*time)
            print(f"You will receive {round(calculate_simple_investment)} by the end of {time} years.")
        elif interest == "compound":
            calculate_compound_investment = principal*(1 + rate)**time
            print(f"You will receive {round(calculate_compound_investment)} by the end of {time} years."  )
      
        break

    elif (selection == "bond"):
        present_value = float(input("Please enter present value of the house: "))
        interest_rate = float(input("Please enter monthly interest rate in percentage: "))
        interest_rate = interest_rate/100/12
        time_repayment = float(input("Please enter number of months you plan to take to repay bond: "))
        repayment = (interest_rate*present_value) / 1 - (1+interest_rate)**(-time_repayment)
        print(f"Your monthly repayments will be {round(repayment)}.")
        break
    else:
        print("Sorry, Invalid input.")
