def main():
    phonebook = {
        "Ali": "0300-1234567",
        "Sara": "0321-7654321",
        "Ahmed": "0345-9876543"
    }

    name = input("Enter name to find phone number: ")
    
    if name in phonebook:
        print(f"{name}'s number: {phonebook[name]}")
    else:
        print("Name not found in phonebook.")

if __name__ == "__main__":
    main()
