

def main():
    
    print("PYTHON GUESSING GAME\n\n")
    
    animal = "python"
    answer = False
    while(not answer or guess == q):
        guess = input("I am thinking of an animal.  "
        "What is it?  ").lower().strip()
        print("your guess is:",guess)
        if(guess == animal):
            answer = True
            print("Lucky guess!  Then again this game IS"
                  " called \nthe PYTHON guessing game.")
        elif(guess == 'q' or guess == 'quit'):
            print("Giving up so soon?  Sissy.")
            break
        else:
            print("Not even close, try again!")
            
if __name__ == "__main__":    
    main()