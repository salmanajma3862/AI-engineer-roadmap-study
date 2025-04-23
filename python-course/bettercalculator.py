num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter another number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        print("num1/num2")
else:
    print("Invalid operator!")