

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

if choice == '1':
    add=num1+num2
    print("Result:", add)
elif choice == '2':
    sub=num1-num2
    print("Result:", sub)
    
elif choice == '3':
    mul=num1*num2
    print("Result:", mul)
elif choice == '4':
    div=num1/num2
    print("Result:", div)
else:
    print("Invalid choice.")
    exit()
print('GOOD BYE')   
