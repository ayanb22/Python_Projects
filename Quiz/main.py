import random
 
beginner = [
        {
            "question" : "What is the capital of India?",
            "options" : ["1) Mumbai ", "2) Delhi", "3) Kolkata" , "4) Chennai" ] ,
            "answer" : 2
        },

        {
            "question" : "Which language is used for web development?",
            "options" : ["1) Python ", "2) Java", "3) HTML" , "4) C++" ] ,
            "answer" : 3
        },

        {
            "question" : "What is 5 + 7?",
            "options" : ["1) 20 ", "2) 5", "3) 10" , "4) 12" ] ,
            "answer" : 4
        },

        {
            "question" : "Which data type is used to store text in Python?",
            "options" : ["1) int ", "2) float", "3) str" , "4) bool" ] ,
            "answer" : 3
        },

        {
            "question" : "Which is called red planet?",
            "options" : ["1) Earth ", "2) Mars", "3) Venus" , "4) Jupiter" ] ,
            "answer" : 2
        }
    ]

medium = [
        {
            "question" : "What is the output of len('Python')?",
            "options" : ["1) 5 ", "2) 6", "3) 7" , "4) Error" ] ,
            "answer" : 2
        },

        {
            "question" : "Which keyword is used to define a function in Python?",
            "options" : ["1) function ", "2) define", "3) def" , "4) fun" ] ,
            "answer" : 3
        },

        {
            "question" : "What is the result of 10 // 3 in Python?",
            "options" : ["1) 3.33 ", "2) 3", "3) 4" , "4) 3.0" ] ,
            "answer" : 2
        },

        {
            "question" : "Which data structure uses key-value pairs?",
            "options" : ["1) List ", "2) Tuple", "3) Dictionary" , "4) Set" ] ,
            "answer" : 3
        },

        {
            "question" : "What will bool(0) return?",
            "options" : ["1) True ", "2) False", "3) 0" , "4) Error" ] ,
            "answer" : 2
        }
    ]
hard = [
        {
            "question" : "What is the output of 3 * '7'?",
            "options" : ["1) 21 ", "2) 777", "3) Error" , "4) 37" ] ,
            "answer" : 2
        },

        {
            "question" : "What is the output of type([])?",
            "options" : ["1) list ", "2) <class'list'>", "3) array" , "4) List" ] ,
            "answer" : 2
        },

        {
            "question" : "What will happen if you access a key that doesn't exist in a dictionary?",
            "options" : ["1) Returns None ", "2) Returns 0", "3) KeyError" , "4) IndexError" ] ,
            "answer" : 3
        },

        {
            "question" : "What is the output of True + True in Python?",
            "options" : ["1) True ", "2) 2", "3) False" , "4) Error" ] ,
            "answer" : 2
        },

        {
            "question" : "Which of the following is immutable?",
            "options" : ["1) List ", "2) Dictionary", "3) Set" , "4) Tuple" ] ,
            "answer" : 4
        }
    ]

def quiz_run(n,m):
    score = 0
    Question_count = 0
    correct = 0
    wrong = 0
   
    # Rules Checking & Start Quiz
    while True:
        response = (input("'Want to check the rules' type 'Rules'for starting the quiz' press 'Start' :"))
        response = response.lower()
        if response == "rules":
            print("For every correct answer you will get 4 points\nfor every wrong one -1 will be deducted")
            response_2 = (input("Type 'Start' for starting the quiz : "))
            response_2 = response_2.lower()
            while response_2 != "start":
                response_2 = input(("Type 'Start' for starting the quiz : "))
                response_2 = response_2.lower()
            print("------------Your Quiz is Starting-----------")
            break
        elif response == "start":
            print("------------Your Quiz is Starting-----------")
            break
        if response != "rules" and response != "start":           
            print("Invalid Response type the correct one")  

    # Printing Question-Option-Answer, Calculating Score, Printing Result                  
    random.shuffle(m)
    for sl_number, q in enumerate(m, start=1):
        print(sl_number, ")", q['question'])
        for option in q["options"]:
            print(option)
        
        while True:
                try:
                    answer = int(input("Enter your answer : "))
                    if answer <1 or answer > len(q["options"]):
                        print("------------Pay Attention it is an Invalid Option number-----------") 
                    elif answer == q["answer"]:
                        print("--------------Correct---------------")
                        correct += 1 
                        score += 4
                        break
                    else:
                        print(f"---------Wrong----------\nThe correct answer is {q['answer']}")
                        score -= 1
                        wrong += 1
                        break
                except ValueError:
                        print(f"-------------Invalid Response, Choose between 1 and {len(q['options'])}------------")

        Question_count += 1       
        if Question_count == n:
            print("-----------------Quiz is ending------------------\n" \
                  "=================================================\n" \
                  "=================================================")
            break 
        else:
            print("-----------------Next Question-------------------\n" \
                  "=================================================\n" \
                  "=================================================")
   
    
    performance = round((correct / n) * 100)
    return score, performance, correct, wrong, Question_count


name = input("Welcome to ABC Quiz Center tell us your name Challenger : ")

while True:
    while True:
        response = input("Type 'Beginner' or 'Medium' or 'Hard' according to your level : ")
        response = response.lower()
        if response == "beginner":
            questions_answer_set = beginner
            break
        elif response == "medium":
            questions_answer_set = medium
            break
        elif response == "hard":
            questions_answer_set = hard
            break
        else:
            print("Invalid response Type the correct one")

    while True:
            try:
                number_of_question = int(input(f"{name} how many questions you want challenge : "))
                if number_of_question <= len(questions_answer_set) and number_of_question > 0:
                    break
                elif number_of_question > len(questions_answer_set):
                    print("There are not that number of questions available in that level")
                elif number_of_question <= 0:
                    print("That is an invalid input")
            except ValueError:
                print("That is an invalid input")

    score, performance, correct, wrong, question_count = quiz_run(number_of_question, questions_answer_set)
    print("===========================================================")

    print("------------------------Result----------------------------")
    print(f"Name : {name}")

    print(f"Questions Attempted : {question_count}")
    print(f"Correct : {correct}")
    print(f"Wrong : {wrong}")
    print(f"Score : {score}")

    if performance >= 80:
        print(f"Performance : {performance}% (Excellent)")
    elif performance >= 60:
        print(f"Performance : {performance}% (Good)")
    elif performance >= 40:
        print(f"Performance : {performance}% (Average)")
    else:
        print(f"Performance : {performance}% (You Need to Perform Better)")


    print("=============================================")

    
    while True:
        replay = input("Do you want to play again?")
        replay = replay.lower()
        if replay == "yes":
            print("Starting a new quiz...")
            break        
        if replay == "no":
            break
        else:
            print("Invalid response, Type Yes or No")
    if replay == "no":
        print("Thanks for playing our game\nHope you love it")
        break
    








