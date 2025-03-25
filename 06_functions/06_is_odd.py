def is_odd(n):
    return n % 2 != 0

def main():
    num = int(input("Enter a number: "))
    print("Is odd?", is_odd(num))

if __name__ == "__main__":
    main()
