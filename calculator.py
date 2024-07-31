def calculator():
    while True:
        try:
            num1 = float(input("Enter Value 1: "))
            num2 = float(input("Enter Value 2: "))
            operator = input("Choose Operator (+, -, *, /): ")

            if operator == '+':
                print("Addition: ", num1 + num2)
            elif operator == '-':
                print("Subtraction: ", num1 - num2)
            elif operator == '*':
                print("Multiplication: ", num1 * num2)
            elif operator == '/':
                if num2 == 0:
                    print("Can't Divide By Zero")
                else:
                    print("Division: ", num1 / num2)
            else:
                print("Enter a valid operator")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        # Ask user if they want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Goodbye!")
            break

calculator()
