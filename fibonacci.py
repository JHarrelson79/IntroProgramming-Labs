#This program will print out the nth element in the fibonacci sequence
def elementFinder(n):
    
    if(n < 0):
        print("Nope!")
    elif(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return elementFinder(n-1)+elementFinder(n-2)

def main():
    
    digit = int(input("Which element of the fibonacci sequence would you like?"))
    answer = elementFinder(digit)
    print(answer) 
    
if __name__ == "__main__":    
    main()        