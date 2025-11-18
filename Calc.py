num1 = float(input("firstnumber: "))
op = input("operator+ _ : ")
num2 = float(input("secondnumber: ")) 

if op == "+": 
    print(num1 + num2) 
elif op == "-":
    print(num1 - num2) 
elif op == "*":
    print(num1 * num2) 
elif op == "/": 
    print(num1 / num2)
else: 
    print("invalid command")