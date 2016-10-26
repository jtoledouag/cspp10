number = (input( "enter a problem:" ))
op = number[1]
num1 = int(number[0])
num2 = int(number[2])
print(op)

if op == "+":
    print ("the result is {}".format(num1 + num2))
elif op == "-":
    print ("the result is {}".format(num1 - num2))
elif op == "*":
    print ("the result is {}".format(num1 * num2))
elif op == "/":
    print ("the result is {}".format(num1 / num2))
elif op == "%":
    print ("the result is {}". format(num1 % num2))