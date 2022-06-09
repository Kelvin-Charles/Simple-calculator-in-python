import subprocess
def addition(n1,n2):
    return n1 + n2
def substraction(n1,n2):
    return n1 - n2
def multiplication(n1,n2):
    return n1 * n2
def division(n1,n2):
    return n1 / n2
operations = {
    "+":addition,
    "-":substraction,
    "*":multiplication,
    "/":division
}

def calculator():
    subprocess.call("clear")
    # If your using windows operating system use "cls" instead of "clear"
    n1 = float(input("Enter Your first number: "))
    for operator in  operations:
        print(operator)
    should_continue = True
    while should_continue:
        selected_operation = input("Choose the operation You want to perfom: ")
        calculation_function = operations[selected_operation]
        n2 = float(input("Enter Your next number: "))
        answer = calculation_function(n1,n2)
        print(f"{n1} {selected_operation} {n2} = {answer}")
        should_continue_status = input(f"Type 'y' to continue with calculating {answer}  or 'n' to start a new calculation and 'q' to exit the program: ")
        if should_continue_status == 'y':
            n1 = answer
        elif should_continue_status == "n":
            should_continue = False
            subprocess.call("clear")
            calculator()
        elif should_continue_status == "q":
            should_continue = False
        else:
            should_continue = False

def kelvin_calculator():
    kelvin_calcultor = calculator()
    return kelvin_calcultor
