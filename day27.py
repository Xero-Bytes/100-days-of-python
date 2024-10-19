# KBJCP
# Step 1: Make the list of the questions, options, answers, and prizes
questions = [
    "What is the capital of France?",
    "Who wrote 'Hamlet'?",
    "Which planet is known as the Red Planet?"
]

options = [
    ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
    ["A) Charles Dickens", "B) J.K. Rowling", "C) William Shakespeare", "D) Mark Twain"],
    ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"]
]

correct_answers = ["B", "C", "B"]
prize_money = [1000, 5000, 10000]

# Step 2: Initialize the total prize money with zero at the start
total_prize = 0

# Step 3: Loop through the questions
for i in range(len(questions)):
    # Display the current question
    print("\nQuestion " + str(i + 1) + ": " + questions[i])
    
    # Display the options for the current question
    for option in options[i]:
        print(option)
    
    # Step 4: Get the player's answer
    answer = input("Your answer (A, B, C, or D): ").upper()

    # Step 5: Check if the answer is correct
    if answer == correct_answers[i]:
        total_prize += prize_money[i]
        print("Correct! You have won", prize_money[i], "!")
    else:
        print("Incorrect! Game over.")
        break  # End the game if the answer is wrong

# Step 6: Display the total prize money won
print(f"\nYou are taking home a total of {total_prize}!")
