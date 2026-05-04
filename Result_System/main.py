
def grade(n):
    subject_marks = {}
    total = 0
 
    science = ["English", "Bengali", "Math", "Physics", "Chemistry", "Biology"]
    commerce = ["English", "Bengali", "Math", "Economics", "Accountancy", "Business"]
    arts = ["English", "Bengali", "Math", "Geography", "History", "Psychology"]

    n = n.lower()
    while True:
        if n == "science":
            n = science
            break
        elif n == "commerce":
            n = commerce
            break
        elif n == "arts":
            n = arts
            break
        else:
            print("It is an invalid response")
            n = input("Tell us your stream : ")

    for subject in n:
        marks = int(input(f"Enter the marks for {subject} : "))
        total += marks
        subject_marks[subject] = marks
        
    maximum_marks = len(n) * 100

    percentage = round((total / maximum_marks) * 100)

    return subject_marks, total, maximum_marks, percentage



name = input("Enter your name : ")
stream = input(f"{name} Tell us your stream : ")
subject_marks , total, maximum_marks, percentage = grade(stream)

if percentage >= 90:
    Grade = "A"
    result = "Pass"
elif percentage <= 89 and percentage >= 75:
    Grade = "B"
    result = "Pass"
elif percentage <= 74 and percentage >= 60:
    Grade = "C"
    result = "Pass"
elif percentage <= 59 and percentage >= 40:
    Grade = "D"
    result = "Pass"
else: 
    Grade = "F"
    result = "Fail"




print(f"Name : {name}")
print(f"Stream : {stream}")
for key , value in subject_marks.items():
    print(f"{key} : {value}")
print(f"Total = {total}/{maximum_marks}")
print(f"Percentage = {percentage}")
print(f"Grade = {Grade}")
print(f"Result = {result}")



