import time

def print_pause(prompt):
    print(prompt)
    time.sleep(0.7)

print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")

items = []

while True:
    print_pause("Please enter the number for the floor you would like to visit:")
    response = input("1. Lobby\n" +
                     "2. Human resources\n" +
                     "3. Engineering department\n")
    if response == "1":
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find "
                    "yourself in the lobby.")
        if "ID card" in items:
            print_pause("The clerk greets you, but she has already "
                        "given you your ID card, so there is nothing "
                        "more to do here now.")
            items.append("ID card")
        else:
            print("The clerk greets you and gives you your ID card.")
            items.append("ID card")
    elif response == "2":
        print_pause("You push the button for the second floor.")
        print_pause("After a few moments, you find yourself in the human resources department.")
        if "handbook" in items:
            print_pause("The HR folks are busy at their desks. "
                        "There doesn't seem to be much to do here.")
        else:
            print_pause("The head of HR greets you.")
            if "ID card" in items:
                print_pause("He looks at your ID card and then "
                            "gives you a copy of the employee handbook.")
                items.append("handbook")
            else:
                print_pause("He has something for you, but says he can't "
                            "give it to you until you go get your ID card.")
    elif response == "3":
        print_pause("You push the button for the third floor.")
        print_pause("After a few moments, you find yourself in the engineering department.")
    print_pause("Where would you like to go next?")