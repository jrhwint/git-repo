# Linear Search Implementation
def linear_search(catalog, treasure):
   
    for aisle, product in enumerate(catalog):
        if product == treasure:
            print(f"Treasure found! '{treasure}' is in aisle {aisle}.")
            return aisle
    raise ValueError(f"The treasure '{treasure}' is nowhere to be found in the catalog.")

# Example usage
treasure_chest = ["Godsword", "Agility Potion", "Cooked Shark", "Mystic Robes", "Ancient Staff", "Toxic Blowpipe"]
search_item = input("What are you searching for? ")

try:
    search_result = linear_search(treasure_chest, search_item)
    print(f"Success! '{search_item}' was located at index {search_result}.")
except ValueError as e:
    print(e)
    