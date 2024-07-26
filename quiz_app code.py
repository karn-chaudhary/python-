
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['question'])
        user_answer = input("Enter your answer: ").lower()
        if user_answer == question['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question['answer'])
    
    print("Quiz complete! Your final score is:", score, "out of", len(questions))

# Questions for the quiz
questions = [
    {"question": "What is the capital of France?\n A. Delhi\n B. Washington, D.C.\n C. Landon\n D. Paris ", "answer": "D"},
    {"question": "what is the capital of utter pradesh?\n A.Lucknow\n B. Patna\n C. Dehradun\n D. Dispur", "answer": "A"},
    {"question": "Which planet is known as the Red Planet?\n A. Earth\n B. Mars\n C. Mercury\n D. Venus   ", "answer": "B"},
    {"question": "What is the powerhouse of the cell?\n A. Mitochondra\n B. Neuron\n C.Glial\n D. Commission ", "answer": "A"},
    {"question": "what is the capital of india?\n A. Delhi\n B. Tokyo\n C. Berlin\n D. Mumbai ", "answer": "A"}
]

run_quiz(questions)
