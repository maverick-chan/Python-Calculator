#Simple Python Calculator v1

#User Input Stage

print("Welcome to the Python Calculator v1!")

while True:
    begin_sequence = input("Please type 'Enter' to launch the calculator (or 'q' to quit): ")
    if begin_sequence.lower() == 'q':
        break
    elif begin_sequence.lower() == 'enter':
        active = True
        
        while active:
            number_1 = input("Enter number 1: ")
            operation = input("Enter operation: ")
            number_2 = input("Enter number 2: ")

            #Operations Stages
            if operation == '+':
                answer = int(number_1) + int(number_2)
                print(answer)
            if operation == '-':
                answer = int(number_1) - int(number_2)
                print(answer)
            if operation == '*':
                answer = int(number_1) * int(number_2)
                print(answer)
            if operation == '/':
                answer = int(number_1) / int(number_2)
                print(answer)

            repeat = input("Would you like to start again (yes or no)? ")
            if repeat == 'no':
                active = False
                        
    else:
        print("You have entered an invalid response. Please try again.")