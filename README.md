Authors: Makeda Lowe and Ashanique Tomlinson
Date Created: 5/4/2026
Course: ITT103
GitHub Public URL to Code: [INSERT YOUR GITHUB LINK HERE]


PROGRAM TITLE: POINT OF SALE (POS) SYSTEM

PURPOSE OF THE PROGRAM:
This program is a menu-driven Point of Sale (POS) system designed for a retail store environment. 
It allows a cashier to process customer purchases in an efficient and organized manner. 

The system simulates real-world retail operations by allowing users to:
- View available products
- Add items to a shopping cart
- Remove items from the cart
- View cart contents
- Calculate totals including tax and discount
- Accept payment and generate a receipt

The program demonstrates the use of functions, loops, conditional statements, dictionaries, and input validation.


HOW TO RUN THE PROGRAM:


1. Ensure Python is installed on your system.
2. Open the file: Lowe.Makeda-POS-ITT103-SP2026.py
3. Run the program using:
   - PyCharm, OR
   - Command Prompt / Terminal:
     python filename.py

4. Follow the on-screen menu:
   1. Display Products
   2. Add to Cart
   3. Remove from Cart
   4. View Cart
   5. Checkout
   6. Exit



PROGRAM FEATURES:


1. PRODUCT MANAGEMENT:
- A predefined product catalog is stored using a dictionary.
- Each product includes price and stock quantity.
- The system ensures stock is available before adding items to cart.

2. SHOPPING CART:
- Users can add items with a specified quantity.
- Items can be removed partially or completely.
- Cart displays item name, quantity, price, and total.

3. CHECKOUT SYSTEM:
- Subtotal is calculated based on items in cart.
- A 10% sales tax is applied.
- A 5% discount is applied if subtotal exceeds $5000.
- System validates payment before completing transaction.

4. RECEIPT GENERATION:
- Displays store header
- Itemized list of purchases
- Subtotal, discount, tax, and total
- Amount paid and change returned
- Thank you message

5. ADDITIONAL FEATURES:
- Low stock alerts when stock is below 5
- Multiple transactions can be processed in one session
- Input validation prevents incorrect entries



MODIFICATIONS / ENHANCEMENTS:


The following improvements were made beyond basic requirements:

- Implemented a discount system (5% over $5000)
- Added low stock alert system
- Included formatted receipt output
- Improved user input validation (handles errors and invalid input)
- Added loop structure for continuous system use
- Used functions to improve modularity and code organization



ASSUMPTIONS:


- All product names must be entered exactly as shown (case insensitive).
- The system runs in a console environment (not graphical).
- Prices and stock values are fixed unless modified in the code.
- Payment must be equal to or greater than total amount.



LIMITATIONS:


- No database integration (data resets when program closes)
- No graphical user interface (GUI)
- No user authentication system
- Limited to predefined products only



CONCLUSION:

This POS system successfully demonstrates key programming concepts such as modular design, 
input validation, loops, and data structures. It provides a functional simulation of a retail 
checkout system and meets the requirements outlined in the assignment.
