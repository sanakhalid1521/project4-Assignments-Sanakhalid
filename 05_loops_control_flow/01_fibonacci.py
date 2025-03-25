def fibonacci(n):
    """
    Prints the first 'n' Fibonacci numbers.
    """
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def main():
    num = int(input("Enter the number of Fibonacci terms: "))
    fibonacci(num)

if __name__ == "__main__":
    main()
