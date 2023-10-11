import random

number = random.randint(1, 100)
attempts = 0

print("\t\t\tWelcome to 'Guess My Number'!")

print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few ateempts as possible.\n")

while True :
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number:
            print("Higher...")
        elif guess > number:
            print("Lower...")
        else:
            print("You guessed it!. The number was",number)
            print("And it only took you",attempts,"tries!")
            break

print("\n\nPress the enter key to quit.")

