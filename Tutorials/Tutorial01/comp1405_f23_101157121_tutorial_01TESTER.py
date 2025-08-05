#Name: Maansinh Jadeja
#Student Number: 101157121

def main():

    userInput = input("Enter your seven-digit phone number? ")

    if(userInput.isnumeric()==False or len(userInput)!=7):
        print("ERROR: PLEASE INPUT A 7 DIGIT NUMBER")
        exit()
        
    

    # print(userInput)

    prefixNum = int(userInput[0:3])
    lineNum = int(userInput[3:])
    # print("LINE NUM: ",lineNum)
    # print(prefixNum)

    # print("Your prefix is ",prefixNum)

    #Multiply the prefix with 500
    product1 = prefixNum*500
    print(f'Your prefix is {prefixNum}. Multiply this by 500, and the result is: {product1}')

    #Add 10 to the result and multiply it by 60, and the result is::
    product2 = (product1+10)*60
    print(f'Add 10 to the result and multiply it by 60, and the result is: {product2}')

    #Your line number is ___. Add this to the previous result 3 times, and the result is
    product3 = (lineNum*3)+product2
    print(f'Your line number is {lineNum}. Add this to the previous result 3 times, and the result is: {product3}')

    #Subtract 600 from that result and divide it by 3, and the result is
    product4 = int((product3-600)/3)
    
    print(f'Subtract 600 from that result and divide it by 3 and the result is: {product4}')


    # userInputNumber = int(userInput)
    # print("THE NUMBER: ",userInputNumber)


main()