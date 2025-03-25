import math

def pythagorean_theorem(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    print("Hypotenuse (C) =", pythagorean_theorem(a, b))

if __name__ == "__main__":
    main()
