#! /usr/bin/python3


#userInput = input("Enter your name: ")

def helloUser(name):

    # Single line comment

    """
    Multi
    line
    comment
    """
    
    '''
    Multi
    line
    comment
    '''

    print("Hello,", userInput)

# helloUser(userInput)


def operators():
    numA = 2
    numB = 10
    # These are operators
    
    # +,  -,  *,  /,  %,  **,  //
    
    # =, +=, ...
    
    # ==, !=, >, <, >=, <= 

    # and, or, not

    # in, not in

def variables():

    # Variables
    myNumber = 10


def dataTypes():

    # Data Types
    myString = "This is a string"

    myInt = 10

    myFloat = 0.0

    myBool = False

    myList = [1, "yo", True, [myString]]

    myTuple = (1, "hi", [myList, ("YO")])

    myDictionary = {'key': "y", (1): True}

    myNone = None

    myRange = range(10)

    print(myRange)
    print(myBool)



def ifstatements():

    # if statements

    userInput = input("Enter name:")

    if userInput == "Daniel":
        print("Yo")

    myList = [1,2,3,4]

    if userInput in myList or 3 in myList:
        print("At least one is true")



def ifElse():

    # if-else statements

    userInput = input("Enter name: ")

    if userInput == "Daniel":
        print("Condition is True")
    else:
        print("Condition is False")


def elIfElse():

    # if-elif-else


    userInput = input("Enter name: ")

    if userInput == "Daniel":
        print("Condition is True")
    elif userInput == "Yo":
        print("elif Condition is True")
    else:
        print("All conditions are false")



def forLoop():

    # for loop

    myList = ["Yo", 1, {"key":[True, 2]}]

    for item in myList:
        print(item)

    for index in range(len(myList)):
        print(myList[index])


def whileLoop():

    # while loop
    
    limit = 4
    attempts = 0

    while attempts < limit:
        print("trying to connect...")
        attempts += 1



whileLoop()




def sumNums(a,b):
    return a + b

print(sumNums(10,5))

x = sumNums(2,2)

y = x + 5

print(y)



