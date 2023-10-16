import time

def print_pause(prompt):
    print(prompt)
    time.sleep(0.7)

print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")

while True:
    print_pause("Please enter the number for the floor you would like to visit:")
    response = input("1. Lobby\n" +
                     "2. Human resources\n" +
                     "3. Engineering department\n")
    if response == "1":
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find yourself in the lobby.")
    elif response == "2":
        print_pause("You push the button for the second floor.")
        print_pause("After a few moments, you find yourself in the human resources department.")
    elif response == "3":
        print_pause("You push the button for the third floor.")
        print_pause("After a few moments, you find yourself in the engineering department.")
    print_pause("Where would you like to go next?")