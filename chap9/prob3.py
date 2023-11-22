class Critter:
    """A vitual pet"""
    def talk(self):
        print("\nHi,I'm an instance of class Critter.")
    def __init__(self,name):
        self.name = name
        print("A new critter has been born!")
        print("Hi. I'm",self.name+"\n")
    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep
    
crit1 = Critter("Poochie")
crit2 = Critter("Randolph")

print("\nPrinting crit1:")
print(crit1)

print("Directly accessing crit1.name:")
print(crit1.name)
