def ones_digit(n):
    return n % 10

def main():
    num = int(input("Enter a number: "))
    print("Ones digit:", ones_digit(num))

if __name__ == "__main__":
    main()
