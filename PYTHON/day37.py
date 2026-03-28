# Q&A Maker Program

# Store questions and answers
questions = [
    {
        "question": "What is the capital of Nepal?",
        "answer": "kathmandu"
    },
    {
        "question": "What is 5 + 7?",
        "answer": "12"
    },
    {
        "question": "Who invented Python?",
        "answer": "guido van rossum"
    },
    {
        "question": "What is the square root of 64?",
        "answer": "8"
    }
]

score = 0

print("Welcome to the Quiz!\n")

# Loop through questions
for q in questions:
    user_answer = input(q["question"] + " ").lower()
    
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is:", q["answer"], "\n")

# Final score
print("Your score is:", score, "/", len(questions))