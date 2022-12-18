# Quiz questions
questions = [
     "Is Python a high-level programming language?",
     "Can Python be used to create iOS or Android apps?",
     "Can you use Python to build desktop applications?",
     "Is it possible to write Python code in a Jupyter notebook?",
     "Can you use Python to perform data analysis?",
    "Is Python often used for web development?",  
    "Can you use Python to create games for consoles like the PlayStation or Xbox?"
]

# Correct answers to the questions
answers = [
    "yes",
    "no",
    "yes",
    "yes",
    "yes",
    "yes",
    "no"
]

# Keep track of the number of correct answers
num_correct = 0

# Ask the questions and check the answers
for i, question in enumerate(questions):
    answer = input(f"{question} (yes/no) ")
    if answer.lower() == answers[i].lower():
        print("Correct!")
        num_correct += 1
    else:
        print("Incorrect.")

# Print the final score
print(f"You got {num_correct} out of {len(questions)} correct.")
