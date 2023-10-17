import time
import random


def print_pause(prompt):
    print(prompt)
    time.sleep(1)


def draw_opponent():
    opponents = ["dragon", "troll", "Super Nasty Villain",
                 "wicked fairie", "Donald Trump"]
    return random.choice(opponents)


def start_game():

    items = []
    opponent = draw_opponent()

    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {opponent} is somewhere around here, "
                f"and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.")

    field(opponent, items)


def field(opponent, items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    response = valid_input("(Please enter 1 or 2).\n")
    if response == "1":
        house(opponent, items)
    elif response == "2":
        cave(opponent, items)


def cave(opponent, items):
    if "sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten "
                    "all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        print_pause("You walk back out to the field.")
        items.append("sword")
    field(opponent, items)


def house(opponent, items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the "
                f"door opens and out steps a {opponent}.")
    print_pause(f"Eep! This is the {opponent}'s house!")
    print_pause(f"The {opponent} attacks you!")
    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    response = valid_input("Would you like to (1) fight or (2) run away?\n")
    if response == "1":
        fight(opponent, items)
    elif response == "2":
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.")
        field(opponent, items)


def fight(opponent, items):
    if "sword" not in items:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {opponent}.")
        print_pause("You have been defeated!")
        print_pause("GAME OVER...")
    else:
        print_pause(f"As the {opponent} moves to attack, "
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your "
                    "hand as you brace yourself for the attack.")
        print_pause(f"But the {opponent} takes one look "
                    "at your shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {opponent}. "
                    "You are victorious!")
    play_again()


def play_again():
    while True:
        response = input("Would you like to play again? (y/n)\n")
        if response == "y":
            print_pause("Excellent! Restarting the game ...")
            start_game()
            break
        if response == "n":
            print_pause("Thanks for playing the game!")
            break


def valid_input(prompt):
    while True:
        response = input(prompt)
        if response in ["1", "2"]:
            return response


start_game()
