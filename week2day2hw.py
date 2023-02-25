class ShoppingCart:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
        
    def show_items(self):
        print(self.items)
        
def main():
    cart = ShoppingCart()
    while True:
        choice = input("What would you like to do? Show/Add/Delete or Quit? ")
        if choice.lower() == "show":
            cart.show_items()
        elif choice.lower() == "add":
            item = input("What would you like to add? ")
            cart.add_item(item)
        elif choice.lower() == "delete":
            item = input("What would you like to delete? ")
            cart.remove_item(item)
        else:
            print("You chose to quit.")
            break
    cart.show_items()
     
main()