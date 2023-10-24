class Dog:
    scientific_name = "Canis lupus familiaris"

    def __init__(self, name):
        self.name = name
        self.woofs = 1

    def count(self):
        for woof in range(self.woofs):
            self.speak()
        self.woofs += 1

    def speak(self):
        print("Woof!")

    def eat(self, food):
        if food == "biscuit":
            print("Yummy!")
        else:
            print("That's not food!")

    def hear(self, words):
        if self.name in words:
            self.speak()


class Cat:

    def __init__(self):
        self.mood = "neutral"

    def speak(self):
        if self.mood == "happy":
            print("purr!")
        elif self.mood == "angry":
            print("Hiss!")
        else:
            print("Meow!")

