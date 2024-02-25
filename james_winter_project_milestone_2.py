class ItemToPurchase:
    def __init__(self):
        # Initialize the attributes for the item
        self.item_name = "none"  # Default name is "none"
        self.item_price = 0      # Default price is $0
        self.item_quantity = 0   # Default quantity is 0
        self.item_description = "none" # Default description is "none"

    def print_item_cost(self):
        # Calculate total cost for the item and print the details
        total_price = self.item_price * self.item_quantity
        # Formats numers if they don't need decimals to the right
        formatted_price = "{:.2f}".format(self.item_price).rstrip('0').rstrip('.')
        formatted_total_price = "{:.2f}".format(total_price).rstrip('0').rstrip('.')
        print(f"{self.item_name} {self.item_quantity} @ ${formatted_price} = ${formatted_total_price}")

class ShoppingCart:

    cart_items = []

    def __init__(self, name="none", date="January 1, 2020"):
        self.customer_name = name
        self.current_date = date

    def add_item(self, ItemToPurchase): # Adds an item to cart_items
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        # Iterate through cart items and remove the item with matching name
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break

        if not found:
            print("Item not found in cart. Nothing removed.")
        
    def modify_item(self, modified_item):
        # Iterate through cart items to find the item to modify
        found = False
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                # If the item is found, update its attributes if new values are provided
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                found = True
                break
    
        # If item not found, print a message
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items
    
    def get_cost_of_cart(self):
        cost = 0
        for item in self.cart_items:
            cost += item.item_price * item.item_quantity

        formatted_cost = "{:.2f}".format(cost).rstrip('0').rstrip('.')
        return(formatted_cost)
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        for item in self.cart_items:
            item.print_item_cost()
        print(f"Total: ${self.get_cost_of_cart()}") # Needs formatting

    def print_description(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu(Cart):
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity') # This changes more than quantity
    print('i - Output items\' descriptions')
    print('o - Output shopping cart')
    print('q - Quit')
    option = str(input('Choose an option: '))
    if option == 'q':
       return option
    elif option == 'a':
        item = ItemToPurchase()
        item.item_name = str(input("Enter the item name: "))
        item.item_price = float(input("Enter the item price: "))
        item.item_quantity = int(input("Enter the item quantity: "))
        item.item_description = str(input("Enter the item description: "))
        Cart.add_item(item)
    elif option == 'r':
        item_name = str(input("Enter the name of the item to remove: "))
        Cart.remove_item(item_name)
    elif option == 'c':
        item_name = str(input("Enter the name of the item to modify: "))
        modified_item = ItemToPurchase()
        modified_item.item_name = item_name
        modified_item.item_price = float(input("Enter the new price of the item: "))
        modified_item.item_quantity = int(input("Enter the new quantity of the item: "))
        modified_item.item_description = str(input("Enter the new description of the item: "))
        Cart.modify_item(modified_item)
    elif option == 'i':
        Cart.print_description()
    elif option == 'o':
        Cart.print_total()

name = str(input("Enter customer name: "))
date = str(input("Enter date: "))
my_cart = ShoppingCart(name, date)
option = "none"
while option != 'q':
    option = print_menu(my_cart)

my_cart.print_total()
my_cart.print_description()


