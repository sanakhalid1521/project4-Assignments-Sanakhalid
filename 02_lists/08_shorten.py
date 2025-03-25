def shorten(lst):
    """
    Returns a list with first and last elements removed.
    """
    return lst[1:-1] if len(lst) > 2 else []

# Starter Code
def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Shortened list:", shorten(numbers))

if __name__ == "__main__":
    main()
