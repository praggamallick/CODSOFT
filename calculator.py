print("CHOOSE + FOR ADDITION\nCHOOSE - FOR SUBTRACTION\nCHOOSE * FOR MULTIPLICATION \nCHOOSE / FOR DIVISION\nCHOOSE ** FOR POWER")


n= input("Enter an operator to perform:")
number1=float(input("Enter the first number:"))
number2=float(input("Enter the second number:"))



if  n == "+":
    output= number1 + number2
    print(output)

elif n == "-":
    output= number1 -number2
    print(output)

elif n == "*":
    output= number1 * number2
    print(output)

elif n == "/":
    output= number1 / number2
    print(output)

elif n == "**":
    output= number1 ** number2
    print(output)