print("Simple Calculator(+,-,*,/)")

op1 = int(input("Enter operand1: "))
op2 = int(input("Enter operand2: "))
operator  = input("Enter the operator: ")

if operator == '+':
    sum = op1 + op2
    print(sum)
elif operator == '-':
    print(op1 - op2)
elif operator == '*':
    print(op1 * op2)
elif operator == '/':
    print(op1/op2)
else:
    print("Invalid operator")
