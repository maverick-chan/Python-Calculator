#Simple Python Calculator v2

print("Welcome to the Python Calculator v2!")

while True:
    begin_sequence = input("Please hit any key to launch the calculator (or 'q' to quit): ")
    if begin_sequence.lower() == 'q':
        break
    else:
        active = True
        answer = None #Initialize the answer variable.
        
        while active:
            number_1 = input("Enter a number: ")
            operation = input("Enter the operation: ")
            number_2 = input("Enter a number: ")


            if operation == '+' or operation == 'addition' or operation == 'add':
                answer = int(number_1) + int(number_2)
                print()
                print(answer)
            elif operation == '-' or operation == 'subtraction' or operation == 'subtract' or operation == 'minus':
                answer = int(number_1) - int(number_2)
                print()
                print(answer)
            elif operation == '*' or operation == 'multiplication' or operation == 'multiply' or operation == 'times' or operation == 'x':
                answer = int(number_1) * int(number_2)
                print()
                print(answer)
            elif operation == '/' or operation == 'division' or operation == 'divide':
                answer = int(number_1) / int(number_2)
                print()                
                print(answer)

            while True:
                next_operation = input("Enter the operation (or 'q' to quit): ")
                if next_operation == 'q':
                    break
                next_number = input("Enter a number: ")

                if next_operation == '+' or next_operation == 'addition' or next_operation == 'add':
                    answer += int(next_number)
                    print()
                    print(answer)
                elif next_operation == '-' or next_operation == 'subtraction' or next_operation == 'subtract' or operation == 'minus':
                    answer -= int(next_number)
                    print()                    
                    print(answer)
                elif next_operation == '*' or next_operation == 'multiplication' or next_operation == 'multiply' or operation == 'times' or operation == 'x':
                    answer *= int(next_number)
                    print()                    
                    print(answer)
                elif next_operation == '/' or next_operation == 'division' or next_operation == 'divide':
                    answer /= int(next_number)
                    print()                    
                    print(answer)

            repeat = input("Would you like to calculate again (yes or no)? ")
            if repeat == 'no':
                active = False