class Critter:
    """A vitual pet"""
    total = 0
    
    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood,"\n")
        
    def __init__(self,name,mood):
        self.name = name
        self.__mood = mood
        print("A new critter has been born")
    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep
    def __private_method(self):
        print("This is a private method.")
    def public_method(self):
        print("This is a public method")
        self.__private_method()
        
crit = Critter(name = "Poochie", mood = "happy")
crit.talk()
crit.public_method()
