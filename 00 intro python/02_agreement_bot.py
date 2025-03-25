def agreement_bot():
    response = input("Do you agree? (yes/no): ").strip().lower()
    if response == "yes":
        print("Great! Let's proceed.")
    else:
        print("You need to agree to continue.")

def main():
    agreement_bot()

if __name__ == "__main__":
    main()
