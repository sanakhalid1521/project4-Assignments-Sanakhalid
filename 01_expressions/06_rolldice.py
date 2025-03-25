import random

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def main():
    num = int(input("How many dice do you want to roll? "))
    print("You rolled:", roll_dice(num))

if __name__ == "__main__":
    main()
