store_items = {"apple": 10, "banana": 5, "orange": 0}

def in_stock(item):
    return store_items.get(item, 0) > 0

def main():
    item = input("Enter item name: ").lower()
    print(f"{item.capitalize()} in stock?", in_stock(item))

if __name__ == "__main__":
    main()
