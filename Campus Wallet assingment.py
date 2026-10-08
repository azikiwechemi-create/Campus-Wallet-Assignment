# I used claude to make sure I met all the requirements in the assignment
# and to check for errors in the code. I also used it to make sure that the code was efficient.

print("Welcome to your Pesapesa!")
print("What is your name?")
name = input()
print(f"Welcome, {name}!!!")


# This is to get the details from the user
print("Available Money in KSH:")
available_money = float(input())
print("Chapati Beans price")
meal_price = float(input())
print("Smocha price:")
snack_price = float(input())
print("Transport cost:")
transport_cost = float(input())


#This is to find out how much money is left after spending on the meal, snack, and transport
total_spending = (meal_price + snack_price + transport_cost)

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# This enables the final result to have a variable that we can use 
remaining_money = available_money - total_spending


#This is to print the receipt of the money
print(f"This is your available money, KSH{GREEN}{available_money}{RESET}")
print(f"This is your total spending, KSH{RED}{total_spending}{RESET}")
if remaining_money < 0:
    print(f"This is your remaining money, KSH{RED}{available_money - total_spending}{RESET}")
elif remaining_money > 0:
    print(f"This is your remaining money, KSH{GREEN}{available_money - total_spending}{RESET}")
print(f"This is your budget for 5 campus days based on your spending, KSH{RED}{total_spending * 5}{RESET}")
print(f"{RED}A negative balance means you need more money{RESET}") 

#This is the plot twist where the user has to pay for printing lecture notes
print("Plot Twist you have decided to buy clothes!")
print("How much did you spend on clothes?")
spending_on_plot_twist = float(input())
total_spending = total_spending + spending_on_plot_twist

remaining_money = available_money - total_spending
print(f"Your new total spending is KSH{RED}{total_spending}{RESET}")
if remaining_money < 0:
    print(f"Your remaining money is KSH{RED}{available_money - total_spending}{RESET}")
elif remaining_money > 0:
    print(f"Your remaining money is KSH{GREEN}{available_money - total_spending}{RESET}")

#This is to check the final balance and give advice to the user
if available_money < total_spending:
    print("Uta inama!!, You need more money!")
elif available_money > total_spending:
    print("You have stuck to your budget and you are good to go!")
if available_money == total_spending:
    print("You have spent all your money and you are broke!")

print("Usi iname!!")
