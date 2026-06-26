class FoodItem:
    def __init__(self,item_id,name,price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def display(self):
        print("item ID: {self.item_id}")
        print("Name: {self.name}")
        print("Price: ₹{self.price}")
        print("-" * 30)