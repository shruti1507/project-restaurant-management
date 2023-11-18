#Shruti Kulashri[RA2311003011195]
#Manasvi[RA2311003011192]
# Define a simple menu with item names and prices
menu = {
    "Burger": 110,
    "Pizza": 180,
    "Pasta": 150,
    "Salad": 200,
    "Drink": 80
}

# Function to display the menu
def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: Rs{price}")

# Function to process orders
def take_order():
    order = {}
    while True:
        display_menu()
        item = input("Enter item to order (or 'done' to finish): ").capitalize()

        if item == 'Done':
            break

        if item in menu:
            quantity = int(input(f"Enter quantity for {item}: "))
            order[item] = quantity
        else:
            print("Invalid item. Please choose from the menu.")

    return order

# Function to calculate the total cost of the order
def calculate_total(order):
    total = sum(menu[item] * quantity for item, quantity in order.items())
    return total
# Main program
def main():
    print("Welcome to the Marriott Restaurant !!")

    # Take an order
    customer_order = take_order()

    # Display the order
    print("\nOrder Summary:")
    for item, quantity in customer_order.items():
        print(f"{item}: {quantity}")

    # Calculate and display the total cost
    total_cost = calculate_total(customer_order)
    print(f"\nTotal Cost: Rs{total_cost}")
    count=0
    if customer_order=='done' or "Done":
        rate=float(input("Please rate our service out of 5:"))
        if rate>=4:
            print("Thank You!!:)")
        else :
            count=1
            remark=input("Please leave your remarks for us where to improve:\n")
            if count==1:
                print("Thank you for your remark we will surely considerate it")

if __name__ == "__main__":
    main()
