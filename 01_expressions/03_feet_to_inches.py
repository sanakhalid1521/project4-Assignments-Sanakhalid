def feet_to_inches(feet):
    return feet * 12

def main():
    feet = float(input("Enter length in feet: "))
    print("Length in inches:", feet_to_inches(feet))

if __name__ == "__main__":
    main()
