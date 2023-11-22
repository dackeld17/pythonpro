import random
import pickle

def load_questions(file_path):
    with open(file_path, 'rb') as file:
        questions = pickle.load(file)
    return questions

def ask_question(question, options):
    print(question)
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
   
    user_answer = input("Your answer : ")
    return int(user_answer)

def run_game(questions):
    random_question = random.choice(questions)
    question, options, correct_answer = random_question
   
    user_answer = ask_question(question, options)
    if user_answer == correct_answer:
        print("\nCorrect!\n")
    else:
        print(f"\nWrong! The correct answer was {correct_answer}\n")

if __name__ == "__main__":
    file_path = "trivia_data.pkl"
    questions = load_questions(file_path)
    run_game(questions)

