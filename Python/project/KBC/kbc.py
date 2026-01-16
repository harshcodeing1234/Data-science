# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.

def kbc(questions,option):
    start_quiz = int(input("Enter 1 for start quiz:"))
    if start_quiz == 1:
        print("==== Welcome to KBC ====")
        print(f"Question: {questions}")

        for idx, opt in enumerate(option[:4], 1):
            print(f"{idx}.{opt}")
        
        answer = input("Enter right option:")

        if answer.lower() == option[4]:
            print(f"Correct answer your answer is {option[4]}")
        else:
            print(f"Incorrect Answer, Answer is {option[4]}")



kbc("Which programing language used in Data science",["java","c++","javaScript","python","python"])




