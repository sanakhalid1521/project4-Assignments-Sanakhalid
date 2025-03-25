import random

def main():
    # User se input lena ke kitne random numbers generate karne hain
    count = int(input("Enter how many random numbers you want: "))

    # Minimum aur maximum range define karna
    MIN_VALUE = 1
    MAX_VALUE = 100

    print("\nGenerated Random Numbers:")
    
    # Loop ke zariye random numbers generate karna
    for _ in range(count):
        print(random.randint(MIN_VALUE, MAX_VALUE))

# Program ko run karne ke liye
if __name__ == "__main__":
    main()
