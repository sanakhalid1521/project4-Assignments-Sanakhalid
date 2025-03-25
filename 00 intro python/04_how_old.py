def calculate_age(birth_year, current_year):
    return current_year - birth_year

def main():
    birth_year = int(input("Enter birth year: "))
    current_year = int(input("Enter current year: "))
    print("You are", calculate_age(birth_year, current_year), "years old.")

if __name__ == "__main__":
    main()
