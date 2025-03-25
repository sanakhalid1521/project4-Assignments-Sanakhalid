def erase_canvas(data):
    """
    Takes a list and clears all elements.
    """
    data.clear()
    return data

# Starter Code
def main():
    data = [1, 2, 3, 4, 5]
    print("Before erase:", data)
    print("After erase:", erase_canvas(data))

if __name__ == "__main__":
    main()
