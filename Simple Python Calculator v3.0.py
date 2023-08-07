#Simple Python Calculator v3.0

def calculator():
    print("Welcome to the Python Calculator v3.0!")
    print("\nEnter 'q' to quit at anytime.")

    active = True
    valid_operators = ['+', '-', '*', '/']

    def get_number_1():
        while True:
            try:
                number = input("Enter a number: ")
                if number == 'q':
                    return None
                number = int(number)
                return number
            except ValueError:
                try:
                    number = float(number)
                    return number
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def get_operator():    
        while True:
            operator = input("Enter the operation ('+', '-', '*', '/'): ")
            if operator == 'q':
                return None
            elif operator not in valid_operators:
                print("Invalid input. Please enter a valid operator ('+', '-', '*', '/')")
            else:
                return operator
            
    def get_number_2():
        while True:
            try:
                number = input("Enter a number: ")
                if number == 'q':
                    return None
                number = int(number)
                return number
            except ValueError:
                try:
                    number = float(number)
                    return number
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            
    def operations():
        number_1 = get_number_1()
        if number_1 == None:
            return False
        operator = get_operator()
        if operator == None:
            return False
        number_2 = get_number_2()
        if number_2 == None:
            return False

        if operator == '+':
            answer = number_1 + number_2
            print()
            print(answer)
        elif operator == '-':
            answer = number_1 - number_2
            print()
            print(answer)
        elif operator == '*':
            answer = number_1 * number_2
            print()
            print(answer)
        elif operator == '/':
            try:
                answer = number_1 / number_2
            except ZeroDivisionError:
                print("You cannot divide by 0!")
            else:
                print()                
                print(answer)
    
    while active:
        operations()

        repeat = input("Would you like to calculate again (yes or no)? ")
        if repeat == 'no':
            active = False

calculator()
