#Name: Maansinh Jadeja
#Student Number: 101157121

def main():

    userNum = input("Please input a number: ")


    if(userNum.isnumeric()==True and int(userNum) >= 1 and int(userNum) <= 9):
        counter=1
        while(counter<=int(userNum)):
            print(str(counter)*counter)
            counter+=1
    else:
        print("ERROR: INVALID INPUT!")


    

main()