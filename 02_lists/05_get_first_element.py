def get_first_element(lst):
    """
    Returns the first element of a list.
    """
    return lst[0] if lst else None

# Starter Code
def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("First element:", get_first_element(numbers))

if __name__ == "__main__":
    main()
