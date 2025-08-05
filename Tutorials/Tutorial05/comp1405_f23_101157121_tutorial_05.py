#Name: Maansinh Jadeja
#Student Number: 101157121


def checkPrime(num):
    for i in range(2,num-1):
        if(num%i==0):
            return False
    return True
    

def main():

    userNum=""

    while(userNum!="-1"):
        userNum=input("Please input a number (-1 to exit): ")

        if(userNum.isnumeric()):
            userNum = int(float(userNum))
            print(checkPrime(userNum))
    

main()


