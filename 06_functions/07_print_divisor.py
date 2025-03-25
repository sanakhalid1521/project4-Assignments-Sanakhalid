def print_divisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

def main():
    num = int(input("Enter a number: "))
    print("Divisors:")
    print_divisors(num)

if __name__ == "__main__":
    main()
