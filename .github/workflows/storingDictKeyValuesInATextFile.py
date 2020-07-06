print('Welcome to the simplest key-value database')
while True:
    
   yourAnswer = input('What do you want to do?\nEnter p to put a new dict key or enter g to get a value from the dict itself or enter l to list all values in a dict or enter q to quit the program. ')

   yourDict = {}

   if yourAnswer == 'p':
       with open("storingPythonText.txt", 'a') as writingDictKeys:
           yourKey = input("What is the name of your key? ")
           yourValue = input("What string value do you want to put into your key? ")
           
           yourDict[yourKey] = yourValue
           writingDictKeys.write(yourKey + ": " + yourDict[yourKey])
           writingDictKeys.write('\n')
           
           
       with open("storingPythonText.txt", 'r') as readingThisFile:
           print(readingThisFile.read())
           break


   elif yourAnswer == 'g':
       with open("storingPythonText.txt", "r") as findingDictValues:
           global desiredWord
           searchedWord = input("what dict value do you want to search for ")
           contents = findingDictValues.read()
           if searchedWord in contents:
               desiredWord = searchedWord
           else:
               print("Your value is not in the file ")
               break
            
       print(desiredWord)
       break 
            
        
           
   elif yourAnswer == 'l':
       
       with open("storingPythonText.txt", 'r') as readingThisFile:
           print(readingThisFile.read())
           break
        
    
   elif yourAnswer == 'q':
       break
