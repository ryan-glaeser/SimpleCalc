from colorama import Fore, Back,  Style, init

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

while (1):
    print ("""
       Select an operation: 
        1. add 
        2. subtract 
        3. multiply
        4. divide
       Enter any other input to exit
       """)

    op = (int(input("Type the number of the operation you wish to perform\n")))
    n1 = (int(input("Enter the first number\n")))
    n2 = (int(input("Enter the second number\n")))

    if op == 1:
        print(Fore.RED, n1, " + ", n2, " = ", add(n1,n2), Style.RESET_ALL)

    elif op == 2:
        print(Fore.RED, n1, " - ", n2, " = ", subtract(n1,n2), Style.RESET_ALL)

    elif op == 3:
        print(Fore.RED, n1, " * ", n2, " = ", multiply(n1,n2), Style.RESET_ALL)

    elif op == 4:
        if (n2 == 0):
            print(Fore.BLACK + Back.WHITE + Style.BRIGHT + "Divide by 0 error", Style.RESET_ALL)
            continue

        else:
            print(Fore.RED, n1, " / ", n2, " = ", divide(n1,n2), Style.RESET_ALL)

    else:
        print("No operation selected, exiting...")
        exit()