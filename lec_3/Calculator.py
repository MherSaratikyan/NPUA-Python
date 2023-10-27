print("Operations:")
print("Enter 'add' for addition")
print("Enter 'sub' for subtraction")
print("Enter 'mul' for multiplication")
print("Enter 'div' for for division")
print("Enter 'quit' for quitting the program")


while True:
    user_input = input("Operation: ")
    if user_input == "quit":
        break
    elif user_input not in ("add", "sub", "mul", "div"):
        print("Please enter a valid operation")
        break
    
    operand1 = float(input("Enter the first operand: "))
    operand2 = float(input("Enter the second operand: "))

    if user_input == "add":
        result = operand1 + operand2
    elif user_input == "sub":
        result = operand1 - operand2
    elif user_input == "mul":
        result = operand1 * operand2
    elif user_input == "div":
        if operand2 == 0:
            print("Error: Attempt to divide by zero")
            continue
        result = operand1 / operand2
    
    print("Result: " + str(result))
    
    