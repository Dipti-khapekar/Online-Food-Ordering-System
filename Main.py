from OnlineFoodOrderingSystem import OnlineFoodOrderingSystem

ofos = OnlineFoodOrderingSystem()

while True:

    print("\n==== Online Food Ordering System ====")
    print("1. Add Food Item")
    print("2. Display Menu")
    print("3. search Food Item")
    print("4. Add To Cart")
    print("5. View Cart")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        ofos.add_food_item()

    elif choice == "2":
        ofos.display_manu()

    elif choice == "3":
        ofos.search_food_item()

    elif choice == "4":
        ofos.add_to_cart()

    elif choice == "5":
        ofos.view_cart()

    elif choice == "6":
        print("Thank you for using Online Food Ordering System!")
        break
    
    else:
        print("Invalid choice.")