def print_events(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

def main():
    num = int(input("Enter a number: "))
    print_events(num)

if __name__ == "__main__":
    main()
