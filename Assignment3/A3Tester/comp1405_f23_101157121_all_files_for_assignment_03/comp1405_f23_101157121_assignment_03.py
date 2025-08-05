#Name: Maansinh Jadeja
#Student Number: 101157121
#Assignment 3
import sys

def main():

    #variables: a,q, e, d are command line arguments
    if(len(sys.argv)!=5):
        print("ERROR: PLEASE ENTER TRUE OR FALSE 4 TIMES AS COMMAND LINE ARGUMENTS")
        exit()

    i = input("Please type true or false: ")
    # print("input: ",i)
    if(i.upper()=="TRUE" or i.upper()=="FALSE"):
        
        #set all the input values to boolean values:
        a = sys.argv[1].upper()=="TRUE"
        i = i.upper()=="TRUE"
        q = sys.argv[2].upper()=="TRUE"
        e = sys.argv[3].upper()=="TRUE"
        d = sys.argv[4].upper()=="TRUE"

        #begin the propositional logic steps 
        step1 = a or i
        step2 = not i 
        step3 = not q
        step4 = not e 
        step5 = not d

        step6 = step1 or step2
        step7 = step3 or step4

        step8 = step7 and step5

        step9 = step6 and step8

        print(f"The Final Result: {step9}")
        
    else:
        print("ERROR: PLEASE ENTER TRUE OR FALSE TO THE INPUT")
        exit()

    # print("a q e d: ",a,q,e,d)

    # print(i)

    # print(f"Arguments: {sys.argv}")



main()