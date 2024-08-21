# basic calculator
# define functions(add, subtract, multiply, division)

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def subtract(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")


def divide(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")


def multiply(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

while True:
    print("A: Addition")
    print("B: Subtraction")
    print("C: Divide")
    print("D: Multiply")
    print("E: Exit")


    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add(a, b)

    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        subtract(a, b)


    elif choice == "c" or choice == "C":
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        divide(a, b)


    elif choice == "d" or choice == "D":
        print("Multiply")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        multiply(a, b)


    elif choice == "e" or choice == "E":
        print("You exited the program.")
        quit()






