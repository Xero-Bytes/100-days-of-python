def ask_question(question, correct_answer):
    user_answer = input(question + " ")
    if user_answer.lower() == correct_answer.lower():
        return True
    else:
        return False

def run_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Simple Quiz Game!")
    print("Answer the following questions:")

    if ask_question("What is the capital of France?", "Paris"):
        print("Correct!")
        score += 1
    else:
        print("Wrong. The correct answer is 'Paris'.")

    if ask_question("What is 5 + 7?", "12"):
        print("Correct!")
        score += 1
    else:
        print("Wrong. The correct answer is '12'.")

    if ask_question("What is the largest mammal?", "Blue whale"):
        print("Correct!")
        score += 1
    else:
        print("Wrong. The correct answer is 'Blue whale'.")

    print(f"\nYour final score is {score} out of {total_questions}.")

# Start the quiz
run_quiz()
