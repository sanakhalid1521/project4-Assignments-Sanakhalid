def add_many_numbers(numbers):
    """
    Takes a list of numbers and returns their sum.
    """
    return sum(numbers)

# Starter Code
def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Sum of numbers:", add_many_numbers(numbers))

if __name__ == "__main__":
    main()
