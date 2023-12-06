class Critter(object):
    """A virtual pet"""

    def __init__(self, name, mood_level=5):
        self.name = name
        self.mood_level = mood_level

    def talk(self):
       
        if self.mood_level >= 8:
            print("I'm", self.name, "and I feel frustrated now.")
        elif 5 <= self.mood_level < 8:
            print("I'm", self.name, "and I feel happy now.")
        elif 2 <= self.mood_level < 5:
            print("I'm", self.name, "and I feel okay now.")
        else:
            print("I'm", self.name, "and I feel mad now.")
           
        self.mood_level -= 2
        if self.mood_level < 0:
            self.mood_level = 0

    def feed(self):
        print("Taste good. Thank you")
        self.mood_level += 3

    def play(self):
        print("Wheee!")
        self.mood_level += 4

    def set_mood(self, level):
        self.mood_level = level

    def get_mood(self):
        return self.mood_level


def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print(
            """
             Critter Caretaker
             0 - Quit
             1 - Listen to your critter
             2 - Feed your critter
             3 - Play with your critter
             """
        )

        choice = input("Choice: ")
        print()

        if choice == "0":
            print("\nPress the enter key to exit")
        elif choice == "1":
            crit.talk()

        elif choice == "2":
            crit.feed()

        elif choice == "3":
            crit.play()

        else:
            print("\nSorry", choice, "isn't a valid choice.")

main()
