def get_list():
    """
    Takes input from user and returns a list of integers.
    """
    return list(map(int, input("Enter numbers separated by space: ").split()))

# Starter Code
def main():
    user_list = get_list()
    print("User list:", user_list)

if __name__ == "__main__":
    main()
