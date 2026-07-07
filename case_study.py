# Restaurant Food Ordering System
# CRUD Operations using Python

menu = []

# Add Food Item
def add_food():
    food_id = int(input("Enter Food ID: "))
    
    # Duplicate ID Check
    for item in menu:
        if item["id"] == food_id:
            print("Food ID already exists!")
            return

    name = input("Enter Food Name: ")
    price = float(input("Enter Price: "))
    availability = input("Available (yes/no): ")

    food = {
        "id": food_id,
        "name": name,
        "price": price,
        "availability": availability
    }

    menu.append(food)
    print("Food item added successfully!\n")


# View All Food Items
def view_menu():
    if len(menu) == 0:
        print("Menu is empty!\n")
        return
 
    print("\n------ RESTAURANT MENU ------")
    print("ID\tName\t\tPrice\tAvailability")
    for item in menu:
        print(f"{item['id']}\t{item['name']}\t\t₹{item['price']}\t{item['availability']}")

    print()


# Search Food Item
def search_food():
    search_name = input("Enter food name to search: ")

    found = False

    for item in menu:
        if item["name"].lower() == search_name.lower():
            print("\nFood Found!")
            print("ID:", item["id"])
            print("Name:", item["name"])
            print("Price: ₹", item["price"])
            print("Availability:", item["availability"])
            found = True

    if not found:
        print("Food item not found!\n")


# Update Food Item
def update_food():
    food_id = int(input("Enter Food ID to update: "))

    for item in menu:
        if item["id"] == food_id:

            print("\n1. Update Price")
            print("2. Update Availability")

            choice = int(input("Enter choice: "))

            if choice == 1:
                new_price = float(input("Enter new price: "))
                item["price"] = new_price
                print("Price updated successfully!\n")

            elif choice == 2:
                new_availability = input("Enter availability (yes/no): ")
                item["availability"] = new_availability
                print("Availability updated successfully!\n")

            else:
                print("Invalid choice!")

            return

    print("Food item not found!\n")


# Delete Food Item
def delete_food():
    food_id = int(input("Enter Food ID to delete: "))

    for item in menu:
        if item["id"] == food_id:
            menu.remove(item)
            print("Food item deleted successfully!\n")
            return

    print("Food item not found!\n")


# Main Program
while True:

    print("====== RESTAURANT FOOD ORDERING SYSTEM ======")
    print("1. Add Food Item")
    print("2. View Menu")
    print("3. Search Food Item")
    print("4. Update Food Item")
    print("5. Delete Food Item")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_food()

    elif choice == 2:
        view_menu()

    elif choice == 3:
        search_food()

    elif choice == 4:
        update_food()

    elif choice == 5:
        delete_food()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid choice! Please try again.\n")
