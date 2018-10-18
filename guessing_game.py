

def main():
    
    print("PYTHON GUESSING GAME\n\n")
    
    animal = "python"
    answer = False
    while(not answer):
        guess = input("I am thinking of an animal.  "
        "What is it?  ").lower().strip()
        print("your guess is:",guess)
        if(guess == animal):
            answer = True
            print("Lucky guess!  Then again this game IS"
                  " called \nthe PYTHON guessing game.")
            response = input("Do you like pythons?  ").lower().strip()   
            if(response[0] is 'y'):
                print("Ok I\'ll let you live.")
            else:
                print("What is wrong with you?!  Pythons are awesome!") 
            
        elif(guess[0] is 'q'):
            print("Giving up so soon?  Sissy.")
            break
        else:
            print("Not even close, try again!")
    
       
if __name__ == "__main__":    
    main()