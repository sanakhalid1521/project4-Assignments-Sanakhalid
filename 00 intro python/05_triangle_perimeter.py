def triangle_perimeter(a, b, c):
    return a + b + c

def main():
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    c = float(input("Enter side 3: "))
    print("Perimeter of triangle:", triangle_perimeter(a, b, c))

if __name__ == "__main__":
    main()
