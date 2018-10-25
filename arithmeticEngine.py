# CMPT 120 - Lab 6
# Jeremy Harrelson
# 25-OCT-2018
##################

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")
    
def showOutro():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come back again soon!")
    
def doLoop():
    while True:
        cmd =  input("What computation do you want to perform? ").lower().strip()
        try:
            num1 = int(input("Enter the first number: "))
        except:
            print("Bad input.  Starting over.")
            continue
        try:
            num2 = int(input("Enter the second number: "))
        except:
            print("Bad input.  Starting over.")
            continue

        try:    
            if cmd == "add":
                result = num1 + num2
            elif cmd == "sub":
                result = num1 - num2
            elif cmd == "mult":
                result = num1*num2
            elif cmd == "div":
                try:
                    result = num1/num2
                except:
                    print("Cant divide by zero!")
                    continue
            elif cmd == "quit":
                break
            else:
                print(cmd,"is not a valid command")
                continue
            print("The result is " + str(result) + ".\n")
        except:
            print("Bad input")
        
def main():
    showIntro()
    doLoop()
    showOutro()
main()