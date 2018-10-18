

def main():
    
    print("PYTHON GUESSING GAME\n\n")
    
    animal = "python"
    answer = False
    while(not answer):
        guess = input("I am thinking of an animal.  "
        "What is it?  ")
        guess.lower().strip()
        if(guess == animal):
            answer = True
            print("Lucky guess!  Then again this game IS"
                  " called \nthe PYTHON guessing game.")
        else:
            print("Not even close, try again!")
            
if __name__ == "__main__":    
    main()