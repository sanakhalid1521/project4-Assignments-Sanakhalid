def double_list(numbers):
    """
    Takes a list and returns a new list with each number doubled.
    """
    return [num * 2 for num in numbers]

# Starter Code
def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Doubled list:", double_list(numbers))

if __name__ == "__main__":
    main()
