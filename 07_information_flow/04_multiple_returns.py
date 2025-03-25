def math_operations(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else None

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    add, sub, mul, div = math_operations(x, y)
    print(f"Addition: {add}, Subtraction: {sub}, Multiplication: {mul}, Division: {div}")

if __name__ == "__main__":
    main()
