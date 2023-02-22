from art import logo
import calculator as calc
import os

def calculator():
    print(logo)
    exit = False
    num1 = float(input("Enter the number 1: "))
    
    while not exit:
        oprt = input("Choose one of the operation from +, -, *, /: ")
        num2 = float(input("Enter the number 2: "))
        result = 0
        match oprt:
            case "+": 
                result = calc.addition(num1,num2)
                print(f"Result of Addition of {num1} and {num2} is => {result}")
            case "-":
                result = calc.subtraction(num1,num2)
                print(f"Result of Subtraction of {num1} and {num2} is => {result}")
            case "*":
                result = calc.multiplication(num1,num2)
                print(f"Result of Multiplication of {num1} and {num2} is => {result}")
            case "/":
                result = calc.division(num1,num2)
                print(f"Result of Multiplication of {num1} and {num2} is => {result}")
            #case "x":
            #    print("Exiting the calculator.")
            #    exit = True
            case _:
                print("Invalid oprtation.")
                
        print(f"Enter 'c' to continue with result {result}")
        print("Enter 'n' for new calculations")
        print("Enter 'x' to exit the calculator")

        choice = input().lower()

        if choice == 'c':
            num1 = result
        if choice == 'n':
            os.system('cls')
            calculator()
        if choice == 'x':
            exit = True
            print("Thank you for using the calculator... Exiting now...")
            

#First call
calculator()
