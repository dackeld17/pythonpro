try:
    num = float(raw_input("Enter a number: "))
except:
    print("Something went wrong!")

try :
    num = float(raw_input("\nEnter a number: "))
except:
    print("That was not a number!")

for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "->",)
        print(float(value))
    except(TypeError,ValueError):
        print("something went wrong!")

for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value,"->",)
        print(float(value))
    except(TypeError):
        print("Can only convert string or number!")
    except(ValueError):
        print("Can only convert a string of digits!")

try:
    num = float(raw_input("\nEnter a number: "))
except ValueError as e:
    print("Not a number! or as Python would say\n",e)

try:
    num = float(raw_input("\nEnter a number: "))
except(ValueError):
    print("That was not a number!")
else:
    print("You entered the number", num)
