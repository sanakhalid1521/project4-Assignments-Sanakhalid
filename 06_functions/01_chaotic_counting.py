import random

def chaotic_counting(n):
    for _ in range(n):
        print(random.randint(1, 100))

def main():
    num = int(input("Enter count limit: "))
    chaotic_counting(num)

if __name__ == "__main__":
    main()
