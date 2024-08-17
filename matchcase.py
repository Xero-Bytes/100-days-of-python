def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error! Division by zero."

def exponential(x, y):
    return x ** y

def floor_division(x, y):
    if y != 0:
        return x // y
    else:
        return "Error! Division by zero."

# Loop to keep the program running
while True:
    print("""
     ________________________________
    |   ~                        ~   |
    |                                |
    |            MAIN MANU           |
    |            ---------           |
    |________________________________|

""")
    print("Select the operation you want:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponential")
    print("7. Floor Division")
    print("8. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

    if choice == '8':
        print("Exiting the calculator. Goodbye!")
        break

    a = int(input("Enter number a: "))
    b = int(input("Enter number b: ")) 

    match choice:
        case '1':
            print("Result = ", add(a, b))
        case '2':
            print("Result = ", subtract(a, b))
        case '3':
            print("Result = ", multiply(a, b))   
        case '4':
            print("Result = ", divide(a, b))  
        case '5':
            print("Result = ", modulus(a, b)) 
        case '6':
            print("Result = ", exponential(a, b))   
        case '7':
            print("Result = ", floor_division(a, b))
        case _:
            print("Invalid input! Please choose a valid operation.")

