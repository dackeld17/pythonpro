name = input("Hi. What's your name? ")
age = int(input("And how old are you? "))
weigh = int(input("Okay, last question. How many people do you weigh? "))

dog = int(age / 7)
print("\nDid you know that you're just",dog,"in dog years?")
seconds = int(age * 365 * 24 * 60 * 60)
print("\nBut you're also over",seconds,"seconds old.")

call = name * 5
print("\nIf a small child were trying to get your attention, your name would become:",call)

moon = weigh/6.0
print("\nDid you know that on the moon you would weight only",moon,"pounds?")

sun = weigh * 27.1
print("But on the sun, you'd weigh",sun,"(but, ah... not for long.)")
