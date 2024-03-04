# Develop a versatile shopping cart program with the following functionalities:
# 1. Upon starting the program, initialize an empty list or dictionary to represent the shopping cart. Present a user-friendly menu that includes the following options:
# 2. Allow users to add items to the shopping cart. For each item, prompt the user to input a name, quantity, and price. Store these details as a dictionary and add it to the shopping cart list.
# 3. Provide the ability to remove items from the shopping cart. Prompt the user to input the name of the item they wish to remove. Ensure to handle cases where the item is not found in the cart.
# 4. Display the current contents of the shopping cart. Include the name, quantity, and price of each item, as well as a running total of the cost.
# 5. Allow the user to exit the program. Upon quitting, print a summary of all items in the cart, including their details and the total cost.
# 6. Implement a loop that continuously prompts the user for their choice until they decide to quit.
# 7. Include appropriate error handling to deal with scenarios such as invalid input when adding or removing items.
# 8. Ensure that the program provides a clear and user-friendly experience. Include informative messages and prompts to guide the user through each step.
# 9. After the user quits, display a friendly closing message along with the final list of items in the cart and the total cost.

your_cart = {} #empty dictionary
while True:    #cycle through options and the result for each
    option = input("What would you like to do today? Add/Remove/Checkout ") #user input
    if option.title() == "Add":   
        product = input("Apples ($1.50 ea), Oranges ($2.00 ea), Bananas ($0.50 ea), Mangos ($3.00 ea), Dragonfruit ($3.00 ea), Papaya ($3.00 ea) or Coconut ($5.00 ea)")
        quantity = float(input("How many? "))

        if product.title() == 'Apples':
            your_cart[product.title()] = 1.5 * quantity
        elif product.title() == 'Oranges':
            your_cart[product] = 2 * quantity
        elif product.title() == 'Bananas':
            your_cart[product] = .5 * quantity
        elif product.title() == 'Mangos':
            your_cart[product] = 3 * quantity
        elif product.title() == 'Dragonfruit':
            your_cart[product] = 3 * quantity
        elif product.title() == 'Papaya':
            your_cart[product] = 3 * quantity
        elif product.title() == 'Coconut':
            your_cart[product] = 5 * quantity
        else:
            print("Please type an available product ")

        

    elif option.title() == "Remove":
        plz_remove = input("What would you like to remove? ")
        if plz_remove.title() == "Apples":
            your_cart.pop('Apples', 'Not in Cart')
        if plz_remove.title() == "Oranges":
            your_cart.pop('Oranges', 'Not in Cart')
        if plz_remove.title() == "Bananas":
            your_cart.pop('Bananas', 'Not in Cart')
        if plz_remove.title() == "Mangos":
            your_cart.pop('Mangos', 'Not in Cart')
        if plz_remove.title() == "Dragonfruit":
            your_cart.pop('Dragonfruit', 'Not in Cart')
        if plz_remove.title() == "Papaya":
            your_cart.pop('Papaya', 'Not in Cart')
        if plz_remove.title() == "Coconut":
            your_cart.pop('Coconut', 'Not in Cart')

    elif option.title() == "Checkout":
        total_price = sum(your_cart.values()) 
        print(your_cart)
        print(f'Your Total: ${total_price:.2f}.')