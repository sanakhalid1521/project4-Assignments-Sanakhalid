def main():
    # User se height input lena (in cm)
    height = int(input("Enter your height in cm: "))

    # Minimum height requirement
    MIN_HEIGHT = 120

    # Check karna ke user ride kar sakta hai ya nahi
    if height >= MIN_HEIGHT:
        print("You are tall enough to ride! 🎢")
    else:
        print("Sorry, you are not tall enough to ride. 😔")

# Program ko run karne ke liye
if __name__ == "__main__":
    main()
