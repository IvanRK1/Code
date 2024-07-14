def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 == 0:
     return "dont division by zero"
    return num1 / num2

while True:
    operator = input("What operation (+, -, *, /)")
    num1 = int(input("Enter num1"))
    num2 = int(input("Enter num2"))
    if operator == "+":
        print(add(num1, num2))
    if operator == "-":
        print(subtract(num1, num2))
    if operator == "*":
        print(multiplication(num1, num2))
    if operator == "/":
        print(division(num1, num2))



