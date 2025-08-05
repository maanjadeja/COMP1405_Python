#Name: Maansinh Jadeja
#Student Number: 101157121

#Non-recursive Function
def capitalizeVowels(characterList:list[str])->list[str]:

    finalList=[]

    for values in characterList:
        if(values in "aeiou"): #Check if any characters contain vowels
            finalList.append(values.upper()) #Add capitalized vowels to new list
        else:
            finalList.append(values) #Add other letters to new list

    # print(finalList)
    return finalList

#Recursive Function
def recursiveCapitalizeVowels(characterList: list[str],index:int=0)->list[str]:
    if(index==len(characterList)): #Return the list if we have gone through the whole list
        return characterList
    else:
        if(characterList[index] in "aeiou"): #Check if any characters contain vowels
            characterList[index]=characterList[index].upper()
        
        index+=1 #Increment index so we can recurse function with new argument to check the next value
        return recursiveCapitalizeVowels(characterList,index)
        

def main():

    listOfCharacters=[]

    # inputCharacter=input("What character would you like to add into the list (0 to exit): ")
    inputCharacter=""

    # print(len(inputCharacter))

    while(len(inputCharacter)<2 and inputCharacter.isnumeric()==False and inputCharacter!="0"): #Ask user to add characters to list
        inputCharacter=input("What character would you like to add into the list (0 to exit): ")
        if(inputCharacter=="0"):
            break
        else:
            listOfCharacters.append(inputCharacter)

    print(listOfCharacters)

    print(f"NON-RECURSIVE: {capitalizeVowels(listOfCharacters)}")
    print(f"RECURSIVE: {recursiveCapitalizeVowels(listOfCharacters)}")


 
    

main()


