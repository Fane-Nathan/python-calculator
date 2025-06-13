"""
A simple calculator function to perform basic arithmetic operations.
"""
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return 'undefined (division by zero)'
    return a / b

def modulus(a, b):
    if b == 0:
        return 'undefined (division by zero)'
    return a % b

def exponentiation(a, b):
    return a ** b


"""
Add floor division to do red-green-refactor from session 20.
"""
def floor_division(a, b):
    if b == 0:
        return 'undefined (division by zero)'
    return a // b

def main():
    b = int(input("Enter the first number: "))
    a = int(input("Enter the second number: "))
    print("Results:")
    print(f"Addition: {addition(a, b)}")
    print(f"Subtraction: {subtraction(a, b)}")
    print(f"Multiplication: {multiplication(a, b)}")
    print(f"Division: {division(a, b)}")
    print(f"Modulus: {modulus(a, b)}")
    print(f"Exponentiation: {exponentiation(a, b)}")

if __name__ == "__main__":
    main()
