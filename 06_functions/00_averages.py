def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def main():
    numbers = list(map(float, input("Enter numbers separated by space: ").split()))
    print("Average:", calculate_average(numbers))

if __name__ == "__main__":
    main()
