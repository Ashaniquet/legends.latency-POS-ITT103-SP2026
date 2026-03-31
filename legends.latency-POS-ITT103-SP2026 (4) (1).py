# Authors: Makeda Lowe and Ashanique Tomlinson
# Date:
# Course: ITT103

Sales_Tax_Rate = 0.10
Discount_Rate = 0.05
Discount_Threshold = 5000.00
Low_Stock_Threshold = 5

# Creates and returns the predefined product catalog.
# Each product has a price and stock quantity.
PRODUCTS = {
        "rice": {"price": 1500.00, "stock": 20},
        "water": {"price": 100.00, "stock": 100},
        "bread": {"price": 500.00, "stock": 50},
        "flour": {"price": 250.00, "stock": 15},
        "sugar": {"price": 150.00, "stock": 12},
        "bleach": {"price": 200.00, "stock": 25},
        "toothpaste": {"price": 500.00, "stock": 50},
        "apple juice": {"price": 350.00, "stock": 10},
        "cooking oil": {"price": 180.00, "stock": 30},
        "eggs": {"price": 2000.00, "stock": 12},
        "snacks": {"price": 150.00, "stock": 50},
        "soap": {"price": 350.00, "stock": 28},
        "cereal": {"price": 800.00, "stock": 13},
        "wash cloth": {"price": 80.00, "stock": 22},}

#HEADER

print("\n   WELCOME TO BEST BUY RETAIL STORE!")

#Display all available products
def display_products(products):

    print("\nProduct Catalog")
    print(f"{'Product':<15}{'Price($)':<14}{'Stock':<10}")
    print("-" * 39)

    for name, details in products.items():
        print(f"{name.title():<15}{details['price']:<14.2f}{details['stock']:<10}")

    print("-" * 39)


def get_menu_choice():
    # Prompts the user for menu choice.
    while True:
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice in ("1", "2", "3", "4", "5", "6"):
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


def get_product_name(products):
    # Prompt the user for a valid product name.
    while True:
        product_name = input("Enter product name: ").strip().lower()

        if product_name in products:
            return product_name
        else:
            print("Invalid product name. Please enter a valid product name from the catalog.")


def get_quantity(prompt):
    # Prompts the user for a valid positive integer.
    while True:
        try:
            quantity = int(input(prompt))
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be greater than zero.")
        except ValueError:
            print("Invalid quantity. Please enter a positive integer.")

# Adds selected products to the shopping cart after
# validates stock availability before adding items to cart
def add_to_cart(products, cart):
    while True:
        display_products(products)
        product_name = get_product_name(products)
        quantity = get_quantity("Enter quantity to add: ")

        available_stock = products[product_name]["stock"]
        current_in_cart = cart[product_name]["quantity"] if product_name in cart else 0
        if  quantity > available_stock:
           print(f"Cannot add that quantity. You already have {current_in_cart} in your cart" 
                 f" and only {available_stock} items are available.")
           continue #go back and try again

        #Add items cart
        if product_name in cart:
           cart[product_name]["quantity"] += quantity
        else:
           cart[product_name] = {
               "price": products[product_name]["price"],
               "quantity": quantity,}

        # Reduce stock
        products[product_name]["stock"] -= quantity
        print(f"\n{quantity} x {product_name.title()} added to cart successfully.")

       #checks if the product stock has fallen below the low stock threshold
        if products[product_name]["stock"] < Low_Stock_Threshold:
             print(f"LOW STOCK ALERT: {product_name.title()} has only {products[product_name]['stock']} left!")
        choice = input("\nDo you want to add another item? (yes/no):").strip().lower()
        if choice != "yes":
            break


    print("\nUpdated Product Catalog:")


def remove_from_cart(products,cart):
  # Removes items from cart (allows the user to remove items completely or partially from shopping cart)
    if not cart:
        print("Cart is empty. Nothing to remove.")
        return

    view_cart(cart)

    product_name = input("Enter product name: ").strip().lower()

    if product_name not in cart:
        print("Invalid product name. Please enter a valid product name from the cart.")
        return

    quantity_to_remove = get_quantity("Enter quantity to remove: ")
    cart_quantity = cart[product_name]["quantity"]

    if quantity_to_remove > cart_quantity:
       print(f"cannot remove {quantity_to_remove}. You only have {cart_quantity} in your cart.")
       return

    elif quantity_to_remove == cart_quantity:
        products[product_name]["stock"] += cart_quantity
        del cart[product_name]
        print(f"{product_name.title()} removed from cart successfully.")

 # Removes only some quantity from shopping cart (not all)
    else:
        cart[product_name]["quantity"] -= quantity_to_remove
        products[product_name]["stock"] += quantity_to_remove
        print(f"{quantity_to_remove} x {product_name.title()} removed from cart successfully.")


    print("\nUpdated Product Catalog:")
    display_products(products)


def view_cart(cart):
    # Displays all items currently in cart
    if not cart:
        print("Cart is empty. Nothing to view.")
        return

    print("\nShopping Cart")
    print(f"{'Item':<15}{'Qty':<8}{'Unit Price($)':<15}{'Total($)':<12}")
    print("-" * 50)

    cart_total = 0

    for item, details in cart.items():
        item_total = details["quantity"] * details["price"]
        cart_total += item_total
        print(f"{item.title():<15}{details['quantity']:<8}{details['price']:<15.2f}{item_total:<12.2f}")

    print("-" * 50)
    print(f"{'Cart Total:':<38}{cart_total:.2f}")
    print("-" * 50)


def calculate_subtotal(cart):
    # Calculates and returns the subtotal of all items in the cart.
    subtotal = 0
    for item, details in cart.items():
        subtotal += details["price"] * details["quantity"]
    return subtotal


def calculate_discount(subtotal):
    # Applies a 5% discount if subtotal is above the threshold.
    if subtotal > Discount_Threshold:
        return subtotal * Discount_Rate
    return 0


def calculate_tax(amount):
    # Calculates sales tax.
    return amount * Sales_Tax_Rate


def checkout(cart):
    # Displays checkout summary.
    if not cart:
        print("Cart is empty. Nothing to check out.")
        return
    # calculate values
    subtotal = calculate_subtotal(cart)
    discount = calculate_discount(subtotal)
    taxable_amount = subtotal - discount
    tax = calculate_tax(taxable_amount)
    total = taxable_amount + tax

    #Show total due
    print(f"\n========CHECKOUT SUMMARY=======")
    print(f"subtotal: ${subtotal:.2f}")
    print(f"discount:-${discount:.2f}")
    print(f"tax: {tax:.2f}")
    print(f"Total Amount Due: ${total:.2f}")
    print("__________________________________")

    # Accept payments with commmas allowed
    while True:
        payment_input = input("Enter payment received: $").replace(",", "")
        try:
            payment = float(payment_input)
        except ValueError:
            print("invalid input. Please enter a number.")
            continue
        if payment < total:
           print("Insufficient funds. Please enter an amount equal to or greater than the total amount.")
        else:
            change = payment - total
            break

    #Gerenating receipt - Header
    print("\n=============================")
    print("BEST BUY RETAIL STORE")
    print("==============================")

   # Display each item purchased
    for item, details in cart.items():
        item_total = details["price"] * details["quantity"]
        print(f"{item.title()} x{details['quantity']} - ${item_total:.2f}")

  # Display cost breakdown
    print("___________________________")
    print(f"subtotal: ${subtotal:.2f}")
    print(f"discount: ${discount:.2f}")
    print(f"tax: ${tax:.2f}")
    print(f"Total Amount: ${total:.2f}")
    print(f"paid: ${payment:.2f}")
    print(f"change: ${change:.2f}")
    print("____________________________")
    print("Thank you for shopping with us.")
    cart.clear()

def display_menu():
    print("\n--- POS Menu ---")
    print("1. Display Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")


def main():
    products = PRODUCTS
    cart = {}

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            display_products(products)
        elif choice == "2":
            add_to_cart(products, cart)
        elif choice == "3":
            remove_from_cart(products, cart)
        elif choice == "4":
            view_cart(cart)
        elif choice == "5":
            checkout(cart)
        elif choice == "6":
            print("Thank you for using the POS system.")
            break
if __name__ == "__main__":
    main()
