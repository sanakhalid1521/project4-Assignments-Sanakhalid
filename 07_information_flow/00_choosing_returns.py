def choose_value(a, b):
    return a if a > b else b

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Greater value:", choose_value(x, y))

if __name__ == "__main__":
    main()
