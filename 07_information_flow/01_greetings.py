def greet(name, time_of_day):
    return f"Good {time_of_day}, {name}!"

def main():
    name = input("Enter your name: ")
    time_of_day = input("Enter time of day (Morning/Afternoon/Evening): ")
    print(greet(name, time_of_day))

if __name__ == "__main__":
    main()
