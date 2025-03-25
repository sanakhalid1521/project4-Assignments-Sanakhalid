def print_events(n):
    """
    Prints all even numbers from 1 to n.
    """
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

# Starter Code
def main():
    n = int(input("Enter a number: "))  # User se input le raha hai
    print("Even numbers up to", n, ":")
    print_events(n)

if __name__ == "__main__":
    main()

