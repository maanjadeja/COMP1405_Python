#Name: Maansinh Jadeja
#Student Number: 101157121

def main():

    tutorialInput=""
    quizInput=""
    assignmentInput=""
    finalExamInput=""

    while((tutorialInput=="" or tutorialInput.isnumeric()==False) or (quizInput=="" or quizInput.isnumeric()==False) or (assignmentInput=="" or assignmentInput.isnumeric()==False) or (finalExamInput=="" or finalExamInput.isnumeric()==False)):
        print("")
        tutorialInput= input("What is your average grade for tutorial marks (10%): ")
        quizInput= input("What is your average grade for quiz marks (30%): ")
        assignmentInput= input("What is your average grade for assignment marks (40%): ")
        finalExamInput= input("What is your average grade for final exam marks (20%): ")

    print("")

    if(0<=float(tutorialInput)<=100 and 0<=float(quizInput)<=100 and 0<=float(assignmentInput)<=100 and 0<=float(finalExamInput)<=100):

        print(f"Tutorial grade: {float(tutorialInput)*0.1}")
        print(f"Quiz grade: {float(quizInput)*0.3}")
        print(f"Assignment grade: {float(assignmentInput)*0.4}")
        print(f"Final Exam grade: {float(finalExamInput)*0.2}")

        finalGrade = float(tutorialInput)*0.1+float(quizInput)*0.3+float(assignmentInput)*0.4+float(finalExamInput)*0.2

        print(f"Final grade: {finalGrade}")

        finalLetterGrade=""

        if(90<=finalGrade<=100):
            finalLetterGrade="A+"
        elif(85<=finalGrade<90):
            finalLetterGrade="A"
        elif(80<=finalGrade<85):
            finalLetterGrade="A-"

        elif(77<=finalGrade<80):
            finalLetterGrade="B+"
        elif(73<=finalGrade<77):
            finalLetterGrade="B"
        elif(70<=finalGrade<73):
            finalLetterGrade="B-"
        
        elif(67<=finalGrade<70):
            finalLetterGrade="C+"
        elif(63<=finalGrade<67):
            finalLetterGrade="C"
        elif(60<=finalGrade<63):
            finalLetterGrade="C-"

        elif(57<=finalGrade<60):
            finalLetterGrade="D+"
        elif(53<=finalGrade<57):
            finalLetterGrade="D"
        elif(50<=finalGrade<53):
            finalLetterGrade="D-"
        
        else:
            finalLetterGrade="F"
        
        print(f"Final Letter Grade: {finalLetterGrade}")
    else:
        print("ERR0R: INVALID GRADE INPUT!")




main()