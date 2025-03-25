def count_even(numbers):
    return sum(1 for num in numbers if num % 2 == 0)

def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Count of even numbers:", count_even(numbers))

if __name__ == "__main__":
    main()

