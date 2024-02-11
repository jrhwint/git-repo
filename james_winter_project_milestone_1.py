class ItemToPurchase:
    def __init__(self):
        # Initialize the attributes for the item
        self.item_name = "none"  # Default name is "none"
        self.item_price = 0      # Default price is $0
        self.item_quantity = 0   # Default quantity is 0

    def print_item_cost(self):
        # Calculate total cost for the item and print the details
        total_price = self.item_price * self.item_quantity
        # Formats numers if they don't need decimals to the right
        formatted_price = "{:.2f}".format(self.item_price).rstrip('0').rstrip('.')
        formatted_total_price = "{:.2f}".format(total_price).rstrip('0').rstrip('.')
        print(f"{self.item_name} {self.item_quantity} @ ${formatted_price} = ${formatted_total_price}")

# Initialize a list to store the items in the shopping cart
shopping_cart = []

# Loop to add items to the shopping cart
for j in range(2):
    # Create a new ItemToPurchase object
    shopping_cart.append(ItemToPurchase())
    
    # Prompt the user to input details for the item
    shopping_cart[j].item_name = str(input("Enter the item name: "))
    shopping_cart[j].item_price = float(input("Enter the item price: "))
    shopping_cart[j].item_quantity = int(input("Enter the item quantity: "))

# Print header for the total cost section
print("\nTOTAL COST")

# Loop through each item in the shopping cart
for item in shopping_cart:
    # Print details for each item in the shopping cart
    item.print_item_cost()

# Calculate total cost of all items in the shopping cart
total_cost = sum(item.item_price * item.item_quantity for item in shopping_cart)

# Print the total cost of all items in the shopping cart
formatted_total_cost = "{:.2f}".format(total_cost).rstrip('0').rstrip('.')
print(f"Total: ${formatted_total_cost}")