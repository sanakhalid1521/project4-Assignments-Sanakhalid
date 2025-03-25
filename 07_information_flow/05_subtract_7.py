def subtract_7(numbers):
    return [num - 7 for num in numbers]

def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("After subtracting 7:", subtract_7(numbers))

if __name__ == "__main__":
    main()
