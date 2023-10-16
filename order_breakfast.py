import time


def ask_again():
    response = ""

    while "no" not in response and "yes" not in response:
        response = input("Would you like to place another order? Please say 'yes' or 'no'\n").lower()
        if "no" in response:
            print("OK, goodbye!")
        elif "yes" in response:
            print("Very good, I'm happy to take another order.")
            time.sleep(0.7)
            ask_choice()
        else:
            print("Sorry, I don't understand.")


def ask_choice():
    response = ""

    while "waffles" not in response and "pancakes" not in response:
        time.sleep(0.7)
        response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print("Waffles it is!")
            time.sleep(0.7)
            print("Your order will be ready shortly.")
            time.sleep(0.7)
            ask_again()
        elif "pancakes" in response:
            print("Pancakes it is!")
            time.sleep(0.7)
            print("Your order will be ready shortly.")
            time.sleep(0.7)
            ask_again()
        else:
            print("Sorry, I don't understand.")


print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(0.7)
print("Today we have two breakfasts available.")
time.sleep(0.7)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(0.7)
print("The second is sweet potato pancakes with butter and syrup.")

ask_choice()

