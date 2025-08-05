#Name: Maansinh Jadeja
#Student Number: 101157121
#Assignment 4
import sys

def main():

       
    userAnswer=input("How many petals: ")
    flowerID=""

    if(userAnswer.isnumeric()==False or int(float(userAnswer))!=4 and int(float(userAnswer))!=7 ):
        print("ERROR: INVALID INPUT")
    else:
        if(int(float(userAnswer))==7):
            flowerID="B"
            print(f"Flower {flowerID}")
        else:
            userAnswer=input("Petal shape: ")
            if(userAnswer.upper()!="HEART" and userAnswer.upper()!="ARROW"):
                print("ERROR: INVALID INPUT")
            else:
                if(userAnswer.upper()=="ARROW"):
                    flowerID="C"
                    print(f"Flower {flowerID}")
                else:
                    userAnswer=input("Center shape: ")
                    if(userAnswer.upper()!="CIRCLE" and userAnswer.upper()!="STAR"):
                        print("ERROR: INVALID INPUT")
                    else:
                        if(userAnswer.upper()=="STAR"):
                            flowerID="F"
                            print(f"Flower {flowerID}")
                        else:
                            userAnswer=input("Center colour: ")
                            if(userAnswer.upper()!="COCOA" and userAnswer.upper()!="DENIM"):
                                print("ERROR: INVALID INPUT")
                            else:
                                if(userAnswer.upper()=="DENIM"):
                                    flowerID="E"
                                    print(f"Flower {flowerID}")
                                else:
                                    userAnswer=input("Petal colour: ")
                                    if(userAnswer.upper()!="CARROT" and userAnswer.upper()!="PINK"):
                                        print("ERROR: INVALID INPUT")
                                    else:
                                        if(userAnswer.upper()=="PINK"):
                                            userAnswer=input("Sepal colour: ")
                                            if(userAnswer.upper()!="TEA" and userAnswer.upper()!="MOSS"):
                                                print("ERROR: INVALID INPUT")
                                            else:
                                                if(userAnswer.upper()=="MOSS"):
                                                    flowerID="G"
                                                    print(f"Flower {flowerID}")
                                                else:
                                                    flowerID="N/A"
                                                    print(f"Flower {flowerID}")
                                        else:
                                            userAnswer=input("Sepal colour: ")
                                            if(userAnswer.upper()!="TEA" and userAnswer.upper()!="MOSS"):
                                                print("ERROR: INVALID INPUT")
                                            else:
                                                if(userAnswer.upper()=="MOSS"):
                                                    flowerID="D"
                                                    print(f"Flower {flowerID}")
                                                else:
                                                    flowerID="A"
                                                    print(f"Flower {flowerID}")



main()