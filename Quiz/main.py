def quiz_score(n):
    score = 0
    Question_count = 0
    questions_answer_set = [
        {
            "question" : "1. What is the capital of India?",
            "options" : ["1) Mumbai ", "2) Delhi", "3) Kolkata" , "4) Chennai" ] ,
            "answer" : 2
        },

        {
            "question" : "2. Which language is used for web development?",
            "options" : ["1) Python ", "2) Java", "3) HTML" , "4) C++" ] ,
            "answer" : 3
        },

        {
            "question" : "3. What is 5 + 7",
            "options" : ["1) 20 ", "2) 5", "3) 10" , "4) 12" ] ,
            "answer" : 4
        },

        {
            "question" : "4. Which data type is used to store text in Python?",
            "options" : ["1) int ", "2) float", "3) str" , "4) bool" ] ,
            "answer" : 3
        },

        {
            "question" : "5. Which is called red planet",
            "options" : ["1) Earth ", "2) Mars", "3) Venus" , "4) Jupiter" ] ,
            "answer" : 2
        }
    ]
    if n > len(questions_answer_set):
        print("There are not that number of questions available")
        return
    elif n <= 0:
        print("You don't have the courage to challenge")
        return
    
    response = int(input("'Want to check the rules' Press 1'for starting the quiz' press 2 :"))
    if response == 1:
        print("For every correct answer you will get 4 points\nfor every wrong one -1 will be deducted")
        input("press 2 for starting the quiz : ")
        print("------------Your Quiz is Starting-----------")
    
    

    for q in questions_answer_set:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = int(input("Enter your answer : "))
        while answer <1 or answer > 4:
            print("------------Pay attention there is only 4 options here-----------")
            for option in q["options"]:
                print(option)
            answer = int(input("Enter your answer : "))
            
        if answer == q["answer"]:
                print("--------------Correct---------------")
                score += 4
        else:
            print("---------Wrong----------")
            score -= 1
        Question_count += 1       
        if Question_count == n:
            break
    
   
    

    return score 

name = input("Welcome to ABC Quiz Center tell us your name Challenger : ")
number_of_question = int(input(f"{name} how mane questions you want challenge : "))
print(f"{name} Your final Score is : {quiz_score(number_of_question)}")

