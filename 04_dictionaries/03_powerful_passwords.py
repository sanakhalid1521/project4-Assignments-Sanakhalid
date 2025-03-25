def check_password_strength(password):
    """
    Returns the strength of a given password.
    """
    strength = {
        "length": len(password) >= 8,
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "digit": any(char.isdigit() for char in password),
        "special_char": any(not char.isalnum() for char in password)
    }

    score = sum(strength.values())

    if score == 5:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

def main():
    password = input("Enter a password: ")
    print("Password Strength:", check_password_strength(password))

if __name__ == "__main__":
    main()
