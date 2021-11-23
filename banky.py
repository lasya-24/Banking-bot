"""

This is a program for chatbot
1. The bot will start with a greeting and self intro and asks for the name of the user.
2. The bot will greet and welcome the person
3. Bot will ask what the user want to do, it will offer a choice of things based upon what the bot is designed for.
4. It will respond to user questions appropriately.
"""
from datetime import datetime

def greet_and_introduce():
    print("Hi! I am banky bot, your personal assistant to help you with bank related queries.")
    print("May I know your name?")
# adding new lines for git push test
# first line
# second line
# Third line

def get_timeofday_greeting():
    current_time = datetime.now()
    timeofday_greeting = "Good Morning"
    if(current_time.hour > 12 and current_time.hour < 17):
        timeofday_greeting = "Good Afternoon"
    elif(current_time.hour >= 17 and current_time.hour < 22):
        timeofday_greeting = "Good Evening"
    elif(current_time.hour >= 22):
        timeofday_greeting = "Hi, That's late"
    return(timeofday_greeting)

def welcome(name):
    messages = "Nice to meet you"
    message = "I can help you with the following: "
    print(f"{get_timeofday_greeting()}, {name}, {messages}, {message}")
    
def show_menu():
    print("1. Get details about how to create an account")
    print("2. What are the different types of accounts")
    print("3. Get details about how to get loans")
    print("4. What are the different types of loans available") 
    print("5. End this chat")
    print("------------------------")
    return(int(input("Enter your choice[1-5]")))
def create_account():
    print("To create an acount you require \n -A Passport Photo \n -Address Proof like Aadhar Card, driving licence \n -Id proof like pan card. ")
def get_loans():
    print("To get loans you must have \n -An Employee payslip or Income Tax returns.")
def account_types():
    print("There are different types of accounts like:\n 1. Savings Account\n 2. Current Account\n 3. Fixed Deposits\n 4. Recurring Deposits\n -Savings is used for individuals.\n -Current account is usally given to business people like shops.\n")
def loan_types():
    print("There are different types of loans like:\n 1. Personal Loans\n 2. Business Loans\n 3. Vechicle Loans\n 4. Gold Loans etc...\n -Personal Loans are given to individuals based on their requirements.\n -Business Loans are given to companies as working capitals.")
def banky():
    greet_and_introduce()
    name = input("Your Name : ")
    welcome(name)
    choice = show_menu()
    while choice != 5 :
        if choice == 1 :
            create_account()
        elif choice == 2:
            account_types()
        elif choice == 3 :
            get_loans()
        elif choice == 4:
            loan_types()
        else:
            print("Sorry! I don't understand that, Only enter the above choices")
        choice = show_menu()
banky()



