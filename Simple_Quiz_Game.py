def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    # Get user input and validate it
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                break
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
    
    # Check if the answer is correct
    if options[answer - 1] == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong! The correct answer is: {correct_answer}\n")
        return 0

def play_quiz():
    score = 0
    questions = [
        {
            "question": "What is the keyword used to define a function in Python?",
            "options": ["def", "function", "func", "define"],
            "correct_answer": "def"
        },
        {
            "question": "Which of the following is not a valid data type in Python?",
            "options": ["int", "str", "float", "double"],
            "correct_answer": "double"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": ["Steven Spielberg", "Christopher Nolan", "James Cameron", "Martin Scorsese"],
            "correct_answer": "Christopher Nolan"
        },
        {
            "question": "Which of these is a Python web framework?",
            "options": ["Django", "Flask", "Rails", "Laravel"],
            "correct_answer": "Django"
        }
    ]
    
    # Ask each question in the quiz
    for q in questions:
        score += ask_question(q["question"], q["options"], q["correct_answer"])

    # Display final score
    print(f"Your final score is: {score}/{len(questions)}")
    if score == len(questions):
        print("Awesome! You got a perfect score! 🎉")
    elif score >= len(questions) // 2:
        print("Good job! You know your stuff! 👍")
    else:
        print("Better luck next time! Keep practicing! 💪")

def main():
    while True:
        print("Welcome to the Simple Quiz Game! 🎮")
        play_quiz()
        
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
