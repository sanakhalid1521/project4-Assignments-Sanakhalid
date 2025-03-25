def is_in_range(n, start, end):
    return start <= n <= end

def main():
    num = int(input("Enter a number: "))
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    print("Is in range?", is_in_range(num, start, end))

if __name__ == "__main__":
    main()
