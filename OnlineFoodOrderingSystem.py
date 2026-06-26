from Order import FoodItem

class OnlineFoodOrderingSystem:
    def __init__(self):
        self.menu = []
        self.cart = []

    def add_food_item(self):
        item_id = int(input("Enter Item ID: "))
        name = input("Enter your Name: ")
        price = int(input("Entem Item Price: "))

        food = FoodItem(self,item_id,name,price)
        self.menu.append(food)

    def display_manu(self):
        pass

    def search_food_item(self):
        food_id = int(input("Enter Item ID to search: "))

    def add_to_cart(self):
        food_id = int(input("Enter Item ID: "))

    def view_cart(self):
        pass
