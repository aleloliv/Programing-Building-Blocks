subtotal = 0.00

while True:
    try:
        childs_meal = float(input("What is the price of a child's meal? "))
        adults_meal = float(input("What is the price of an adult's meal? "))

        childs_drink = float(input("What is the price of a child's drink? "))
        adults_drink = float(input("What is the price of an adult's drink? "))

        children_num = int(input("Please, how many children are there? "))
        adults_num = int(input("Please, how many adults are there? "))

        subtotal = (childs_meal * children_num) + (childs_drink*children_num) + (adults_meal * adults_num) + (adults_drink * adults_num)
        
        tax_rate = float(input("What is the sales tax rate? ")) / 100
        sales_tax = subtotal * tax_rate 

        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")

        total = subtotal + sales_tax

        print(f"Total: ${total:.2f}")

        payment = float(input("What is the payment amount? "))

        change = payment - total

        print(f"Change: ${change:.2f}")

        choice = input("Do you wish to continue? YES or NO: ")

        while choice.lower() not in ["yes", "no"]:
            print("Please select YES or NO.")
            choice = input("Do you wish to continue? YES / NO: ").lower()

        if choice.lower() == "no":
            subtotal = 0.00
            break

        subtotal = 0.00  # Reset subtotal for the next iteration

    except ValueError:
        print("Invalid input. Please enter a valid number.")