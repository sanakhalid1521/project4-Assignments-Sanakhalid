import random

def roll_dice():
    return random.randint(1, 6)

def main():
    input("Press Enter to roll the dice... ")
    print("You rolled a:", roll_dice())

if __name__ == "__main__":
    main()
