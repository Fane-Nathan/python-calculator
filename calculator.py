def calculator(a, b):
    """
    A simple calculator function to perform basic arithmetic operations.
    """
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b if b != 0 else 'undefined (division by zero)',
        'modulus': a % b if b != 0 else 'undefined (division by zero)',
        'exponentiation': a ** b,
    }

def main():
    b = int(input("Enter the first number: "))
    a = int(input("Enter the second number: "))
    results = calculator(a, b)
    print("Results:")
    for operation, result in results.items():
        print(f"{operation.capitalize()}: {result}")

if __name__ == "__main__":
    main()
