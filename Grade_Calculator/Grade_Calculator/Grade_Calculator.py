grade = float(input("What is your grade percentage? ")) #gets the grade from the student
letter = "A" #sets the variable letter to a random grade

calculator = True

while (calculator == True):
    if (grade >= 90 and grade < 101): #starts a if statement with the grade
        letter = "A" #sets the variable letter
        calculator = False 
    elif (grade >= 80 and grade < 90):
        letter = "B"
        calculator = False
    elif (grade >= 70 and grade < 80):
        letter = "C"
        calculator = False
    elif (grade >= 60 and grade < 70):
        letter = "D"
        calculator = False
    elif (grade >= 0 and grade < 60):
        letter = "F"
        calculator = False
    else:
        print ("Type a number betwen 0 and 100")
        grade = float(input())

_decimal = grade % 10
if (_decimal >= 7):
    letter += "+"
elif (_decimal < 3):
    letter += "-"

if (grade == 100):
    letter = "A"

if (letter == "A+"):
    letter = "A"
elif (letter == "F+" or letter == "F-"):
    letter = "F"

print("Your grade is: "+letter)

if (grade >= 70):
    print("Congratulations! You have passed the exam!")
else:
    print("I'm sorry, you didn't pass, better luck next time.")



