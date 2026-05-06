def stream_choice(n):

    science = ["English", "Bengali", "Math", "Physics", "Chemistry", "Biology"]
    commerce = ["English", "Bengali", "Math", "Economics", "Accountancy", "Business"]
    arts = ["English", "Bengali", "Math", "Geography", "History", "Psychology"]

    n = n.lower().strip()
    while True:
        if n == "science":
            subject_choice = science
            break
        elif n == "commerce":
            subject_choice = commerce
            break
        elif n == "arts":
            subject_choice = arts
            break
        else:
            print("It is an invalid response")
            n = input("Tell us your stream : ")
            n = n.lower().strip()

    return subject_choice
    
def marks_input(subject_choice):
    subject_marks = {}
    
 

    for subject in subject_choice:
        while True:
            try:
                marks = int(input(f"Enter the marks for {subject} : "))
                if marks < 0 or marks > 100:
                    print("Thats an invalid input please enter a marks between 0-100")
                else:
                    subject_marks[subject] = marks
                    print("===================================")
                    break
            except ValueError:
                print("Enter a valid input : ")
            
        
        
    return subject_marks


def result(subject_marks):

    print("\n========== RESULT ==========\n")
    total = sum(subject_marks.values())     
    maximum_marks = len(subject_marks) * 100
    percentage = round((total / maximum_marks) * 100)
    average = round(total/len(subject_marks))
    highest_marks =  max(subject_marks, key=subject_marks.get)
    lowest_marks =  min(subject_marks, key=subject_marks.get)
    

    if percentage >= 90:
        grade = "A"
        remarks = "Pass"
    elif percentage >= 75:
        grade = "B"
        remarks = "Pass"
    elif percentage >= 60:
        grade = "C"
        remarks = "Pass"
    elif percentage >= 40:
        grade = "D"
        remarks = "Pass"
    else: 
        grade = "F"
        remarks = "Fail"

    return total, maximum_marks, percentage, grade, remarks, average, lowest_marks, highest_marks


while True:
    name = input("Enter your name : ")
    stream = input(f"{name} Tell us your stream : ")
    subjects = stream_choice(stream)
    subject_marks = marks_input(subjects)
    total, maximum_marks, percentage, grade, remarks, average, lowest_marks, highest_marks = result(subject_marks)
    print(f"Name : {name}")
    print(f"Stream : {stream.strip().capitalize()}")
    for key , value in subject_marks.items():
        print(f"{key:<12} : {value}")
    print(f"Total = {total}/{maximum_marks}")
    print(f"Average : {average}")
    print(f"Percentage = {percentage}")
    print(f"Highest: {highest_marks} ({subject_marks[highest_marks]})")
    print(f"Lowest: {lowest_marks} ({subject_marks[lowest_marks]})")
    print(f"Grade = {grade}")
    print(f"Result = {remarks}")

    while True:
        response = input("Do you want to calculate another result : ")
        response = response.lower().strip()
        if response == "yes":
            print("-----------Your result calculation is starting----------")
            break
        elif response == "no":
            print("------ Thanks for visiting --------")
            break
        else:
            print("That is an invalid response, please type 'yes' or 'no'")
    if response == "no":
        break



