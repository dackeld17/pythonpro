class Critter:
    """A vitual pet"""
    total = 0
    
    def talk(self):
        print("\nHi, I'm", self.name)
        
    def __init__(self,name):
        self.name = name
        
        print("A new critter has been born!")
    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep
    def __private_method(self):
        print("This is a private method.")
    def public_method(self):
        print("This is a public method")
        self.__private_method()
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        if new_name == "":
            print("\nA Critter's name can't be empty string.")
        else:
            self.__name = new_name
            print("\nName change successful.")
            
    name = property(get_name, set_name)

crit = Critter("Poochie")
crit.talk()
print("\nMY critter's name is :",crit.get_name())
crit.set_name("")
crit.set_name("Randolph")
print("\nHi, I'm", crit.get_name())
