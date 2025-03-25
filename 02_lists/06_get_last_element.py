def get_last_element(lst):
    """
    Returns the last element of a list.
    """
    return lst[-1] if lst else None

# Starter Code
def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Last element:", get_last_element(numbers))

if __name__ == "__main__":
    main()
