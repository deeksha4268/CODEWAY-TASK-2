def adding(x, y):
    return x + y

def subtracting(x, y):
    return x - y

def multiplying(x, y):
    return x * y

def dividing(x, y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

a= float(input("Enter first number: "))
b= float(input("Enter second number: "))

if choice == '1':
    print("Result:", adding(a,b))
elif choice == '2':
    print("Result:", subtracting(a,b))
elif choice == '3':
    print("Result:", multiplying(a,b))
elif choice == '4':
    print("Result:", dividing(a,b))
else:
    print("Invalid input")
