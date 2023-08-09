#Simple Python Calculator v2.1

print("Welcome to the Python Calculator v2.1!")
print("\nEnter 'q' to quit at anytime.")

active = True
answer = None
valid_operators = ['+', '-', '*', '-']
  
while active:
    number_1 = input("Enter a number: ")
    if number_1 == 'q':
        break
    operation = input("Enter the operation ('+', '-', '*', '/'): ")
    if operation == 'q':
        break
    #if operation not in valid_operators:
        #print("Please enter a valid operator ('+', '-', '*', '/').")
    #else:
    number_2 = input("Enter a number: ")
    if number_2 == 'q':
        break


    if operation == '+':
        answer = int(number_1) + int(number_2)
        print()
        print(answer)
    elif operation == '-':
        answer = int(number_1) - int(number_2)
        print()
        print(answer)
    elif operation == '*':
        answer = int(number_1) * int(number_2)
        print()
        print(answer)
    elif operation == '/':
        try:
            answer = int(number_1) / int(number_2)
        except ZeroDivisionError:
            print("You can't divide by 0!")
        else:
            print()                
            print(answer)
        

    while answer:
        next_operation = input("Enter the next operation: ")
        if next_operation == 'q':
            break
        #elif next_operation not in valid_operators:
            #print("Please enter a valid operator ('+', '-', '*', '/').")
        next_number = input("Enter a number: ")
        if next_number == 'q':
            break

        if next_operation == '+':
            answer += int(next_number)
            print()
            print(answer)
        elif next_operation == '-':
            answer -= int(next_number)
            print()                    
            print(answer)
        elif next_operation == '*':
            answer *= int(next_number)
            print()                    
            print(answer)
        elif next_operation == '/':
            try:
                answer /= int(next_number)
            except ZeroDivisionError:
                print("You can't divide by 0!")
            else:
                print()                    
                print(answer)


    repeat = input("Would you like to calculate again (yes or no)? ")
    if repeat == 'no':
        active = False

#     while answer:
#         next_operation = input("Enter the next operation: ")
#         if next_operation == 'q':
#             break
#         #elif next_operation not in valid_operators:
#             #print("Please enter a valid operator ('+', '-', '*', '/').")
#         next_number = input("Enter a number: ")
#         if next_number == 'q':
#             break

#         if next_operation == '+':
#             answer += int(next_number)
#             print()
#             print(answer)
#         elif next_operation == '-':
#             answer -= int(next_number)
#             print()                    
#             print(answer)
#         elif next_operation == '*':
#             answer *= int(next_number)
#             print()                    
#             print(answer)
#         elif next_operation == '/':
#             try:
#                 answer /= int(next_number)
#             except ZeroDivisionError:
#                 print("You cannot divide by 0!")
#             else:
#                 print()                    
#                 print(answer)