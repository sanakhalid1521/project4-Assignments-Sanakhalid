def print_multiples(n, limit=10):
    for i in range(1, limit + 1):
        print(n * i)

def main():
    num = int(input("Enter a number: "))
    print(f"Multiples of {num}:")
    print_multiples(num)

if __name__ == "__main__":
    main()
