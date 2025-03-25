def energy(mass):
    c = 299792458  # Speed of light in meters per second
    return mass * c**2

def main():
    mass = float(input("Enter mass in kg: "))
    print("Energy (E) =", energy(mass), "Joules")

if __name__ == "__main__":
    main()
