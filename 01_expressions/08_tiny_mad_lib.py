def mad_libs(name, place, activity):
    return f"{name} went to {place} and started {activity}!"

def main():
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    activity = input("Enter an activity: ")
    print(mad_libs(name, place, activity))

if __name__ == "__main__":
    main()
