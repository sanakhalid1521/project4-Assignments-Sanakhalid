def main():
    shop_inventory = {
        "Shirt": 50,
        "Jeans": 30,
        "Shoes": 20
    }

    item = input("Enter item name: ")

    if item in shop_inventory:
        print(f"We have {shop_inventory[item]} {item}(s) in stock.")
    else:
        print(f"Sorry, {item} is not available.")

if __name__ == "__main__":
    main()
