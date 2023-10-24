import random
words = ["APPLE", "BANANA", "ORANGE"]
word = random.choice(words)
letters = ""
chances = 6
hangman_stages = [
    """
    --------
    |      |
    |       
    |
    |
    |
---------------
    """,
    """
    --------
    |      | 
    |      o
    |
    |
    |
---------------
    """,
    """
    --------
    |      |
    |      o
    |      |
    |
    |
---------------
    """,
    """
    --------
    |      |
    |      o
    |      |\\
    |
    |
---------------
    """,
    """
    --------
    |      |
    |      o
    |     /|\\
    |
    |
---------------
    """,
    """
    --------
    |      |
    |      o
    |     /|\\
    |     /
    |
---------------
    """,
    """
    --------
    |      |
    |      o
    |     /|\\
    |     / \\
    |
---------------
    """
]

while chances > 0:
    success = True
    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            success = False
    print()

    if success:
        print("CORRECT !")
        break

    letter = input("Enter your guess: ")

    if letter not in letters:
        letters += letter

    if letter in word:
        print("\nYes!", letter, "is in the word!")
    else:
        print("\nWrong!")
        chances -= 1  

    print(hangman_stages[6 - chances])

if chances == 0:
    print("So far, the word is:\n",word)


