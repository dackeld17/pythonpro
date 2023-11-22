class Critter:
    """A vitual pet"""
    def talk(self):
        print("\nHi,I'm an instance of class Critter.")
    def __init__(self):
        print("A new critter has been born!")
crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()
