import random

words = ['difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university']
word = random.choice(words)

print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.")
print("\nLength of the selected word:", len(word))

correct_letters = ["_"] * len(word)
guessed_letters = set()

max_attempt = 6
attempt = 0

while attempt < max_attempt:
    print("Remaining attempts: ", max_attempt - attempt)
    print("Current guessed word:", " ".join(correct_letters))
    guess = input("Guess a letter: ").lower()
    guessed_letters.add(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                correct_letters[i] = guess
        if "_" not in correct_letters:
            print("Congratulation! You guesse the word:", word)
            break
    else:
        print("Incorrect guess.")
        attempt += 1
        if attempt >= max_attempt:
            print("You've used up all your attempts! The correct word was", word,end = ".")

