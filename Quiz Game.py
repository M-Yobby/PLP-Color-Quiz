choose_color = input("Pick a color: ").strip().lower()  # Get user color choice
# Color Category Identifier
# This program categorizes a color based on user input
category = None  # Initialize category variable 
if choose_color in ["red", "green", "blue"]:
    category = "primary"
elif choose_color in ["yellow", "cyan", "magenta"]:
    category = "secondary"
elif choose_color in ["orange", "purple", "pink"]:
    category = "tertiary"
elif choose_color in ["black", "white", "gray"]:
    category = "neutral"
elif choose_color in ["brown", "gold", "silver"]:
    category = "metallic"
elif choose_color in ["teal", "navy", "olive"]:
    category = "earthy"
else:
    category = "unknown"

print("You chose the color " + choose_color + ".") # Debug: Show chosen color
choose_category = input("Enter the category: ").strip().lower()  # Get user category choice
if category == "unknown": # If the color is unknown
    print("The color " + choose_color + " is not in the list of known colors.") # Debug: Show unknown color
elif choose_category == category: # If the user's category matches the identified category
    print("Correct! " + choose_color + " is a " + category + " color.") # Debug: Show correct category
else: # If the user's category does not match the identified category
    print("Incorrect. " + choose_color + " is not a " + choose_category + " color.") # Debug: Show incorrect category