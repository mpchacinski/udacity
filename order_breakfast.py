import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def ask_again():
    response = ""

    while "no" not in response and "yes" not in response:
        response = input("Would you like to place another order? Please say 'yes' or 'no'\n").lower()
        if "no" in response:
            print_pause("OK, goodbye!")
        elif "yes" in response:
            print_pause("Very good, I'm happy to take another order.")
            ask_choice()
        else:
            print_pause("Sorry, I don't understand.")


def ask_choice():
    response = ""

    while "waffles" not in response and "pancakes" not in response:
        response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print_pause("Waffles it is!")
            print_pause("Your order will be ready shortly.")
            ask_again()
        elif "pancakes" in response:
            print_pause("Pancakes it is!")
            print_pause("Your order will be ready shortly.")
            ask_again()
        else:
            print_pause("Sorry, I don't understand.")


print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")

ask_choice()
