#added a counting to the number of items in list. Added allignment to the list. Added an option to change the price of an item of the list.

print("Hello and welcome to the Shopping Cart Program!\n")
choice = None

shopping_list = []
price_list = []
list_index = 0
total = 0.00
count = 0
price = 0.00

while choice != 6:
    print("\nPlease select one of the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Change the price of an item\n6. Quit")
    choice = int(input("Please enter an action: "))

    if (choice == 1):
        item = input("What item would you like to add? ")
        shopping_list.append(item)
        price = float(input(f"What is the price of {item}? "))
        price_list.append(price)
        print(f"'{item}' has been added to the cart.")
        count += 1

    if (choice == 2):
        print(f"The contens of the shopping cart are:")
        print(f"Number of items in list: {count}")
        for i in range(len(shopping_list)):
            print(f"{i+1}. {shopping_list[i] : <10} - "+f"${price_list[i]:<5.2f}")

    if (choice == 3):
        list_index = int(input("Which item would you like to remove? "))
        shopping_list.pop(list_index-1)
        price_list.pop(list_index-1)
        print("Item removed.")
        count -= 1

    if (choice == 4):
        for i in range(len(price_list)):
            total += price_list[i]
        print(f"The total price of the intems in the shopping cart is ${total:.2f}")
        total = 0.00

    if (choice == 5):
        list_index = int(input("Which item would you like to change? "))
        price = float(input(f"What is the new price for {shopping_list[list_index-1]}? "))
        price_list[list_index-1] = price
        print("Price changed.")

print("Thank you. Goodbye.")