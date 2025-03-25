def count_numbers(lst):
    """
    Counts occurrences of numbers in a list.
    """
    num_count = {}
    for num in lst:
        num_count[num] = num_count.get(num, 0) + 1
    return num_count

def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Number counts:", count_numbers(numbers))

if __name__ == "__main__":
    main()
