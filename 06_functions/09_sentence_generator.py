import random

subjects = ["Ali", "Sara", "Bilal", "Aisha"]
verbs = ["eats", "plays", "reads", "writes"]
objects = ["pizza", "football", "book", "letter"]

def generate_sentence():
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."

def main():
    print("Random sentence:", generate_sentence())

if __name__ == "__main__":
    main()
