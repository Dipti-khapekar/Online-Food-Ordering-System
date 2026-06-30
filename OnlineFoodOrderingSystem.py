from Order import FoodItem

class OnlineFoodOrderingSystem:
    def __init__(self):
        self.menu = []
        self.cart = []

    def add_food_item(self):
        item_id = int(input("Enter Item ID: "))
        name = input("Enter your Name: ")
        price = int(input("Entem Item Price: "))

        food = FoodItem(item_id,name,price)
        self.menu.append(food)

    def display_manu(self):
        if len(self.menu) == 0:
            print("Menu is Empty.")
        else:
            print("\n--MENU--")
            for item in self.menu:
                item.display()

    def search_food_item(self):
        food_id = int(input("Enter Item ID to search: "))

        for item in self.menu:
            if item.item_id == food_id:
                print("Food Item Found.")
                item.display()
                return
            
        print("Food Item Not Found.")

    def add_to_cart(self):
        food_id = int(input("Enter Item ID: "))

        for item in self.menu:
            if item.item_id == food_id:
                self.cart.append(item)
                print("Item Added to Cart successfully!")
                return
            
        print("Item Not Found.")

    def view_cart(self):
        pass
