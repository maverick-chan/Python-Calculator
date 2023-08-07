#Simple Python Calculator v3.1

def calculator():
    print("Welcome to the Python Calculator v3.1!")
    print("Enter 'q' to quit at anytime.\n")

    active = True
    valid_operators = ['+', '-', '*', '/']

    def get_number():
    #Returns integers or decimal numbers
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
    #Returns a valid operator
        while True:
            operator = input("Enter the operation ('+', '-', '*', '/'): ")
            if operator == 'q':
                return None
            elif operator not in valid_operators:
                print("Invalid input. Please enter a valid operator ('+', '-', '*', '/')")
            else:
                return operator
                      
    def operations():
    #Returns the first number in sequence
        number_1 = get_number()
        if number_1 is None:
            return False
        
        answer = number_1
    
    #Returns initial and subsequent operation and number in the equation
        while True:
            operator = get_operator()
            if operator == None:
                return False
            number_2 = get_number()
            if number_2 is None:
                return False

            if operator == '+':
                answer += number_2
                print(f"\n{answer}\n")
            elif operator == '-':
                answer -= number_2
                print(f"\n{answer}\n")
            elif operator == '*':
                answer *= number_2
                print(f"\n{answer}\n")
            elif operator == '/':
                try:
                    answer /= number_2
                except ZeroDivisionError:
                    print("\nYou cannot divide by 0!\n")
                else:             
                    print(f"\n{answer}\n")
    
    while active:
    #Main function with an exit and repeat sequence
        operations()

        repeat = input("Would you like to calculate again (yes or no)? ")
        if repeat == 'no':
            active = False
        elif repeat == 'yes':
            continue
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

calculator()
