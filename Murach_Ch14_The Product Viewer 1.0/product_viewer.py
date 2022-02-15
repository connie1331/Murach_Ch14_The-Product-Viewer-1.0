#******************************************************************************
# Author:           Joel Murach
# Date:             02.15.2022
# Description:      An example from Murach's Python textbook
#                   The product_viewer (product_viewer.py) contains the main code of the program.
#                   This code imports the Products class from the objects module. Then, this code defines functions
#                   that make up the program.
# Function(s)       1. The show_products() function displays a numbered list of products. It accepts a parameter
#                   that's a list  that contains one or more Product objects.
#                   2. The show_product() function displays the data that's available from a product. It accepts a
#                   a parameter that is a Product object. Then, it uses the three attributes of the product to display
#                   the name, price, and discount percent. Finally, it uses the two methods of the products to display
#                   discount amount
#                   3. The main() function that do the following:
#                       - Create the tuple of Product objects
#                       - Display the numbered list of product by passing the tuple to the show_products()function
#                       defined earlier in the module
#                       - Prompt the user to enter a number that corresponds with a product.
#                       - Get the corresponding Product object from the tuple of the Product objects
#                       - Display data of the product object by passing the object to the show_product()
# Sources:          Murach's Python Programming - Beginner
#                   Chapter 14_ How to define and use your own classes
#                   Example: The Product Viewer program 1.0
#******************************************************************************

from objects import Product

def show_products(products):
    print("PRODUCTS")
    for i in range(len(products)):
        product = products[i]
        print(str(i+1) + ". " + product.name)

def show_product(product):
    print("PRODUCT DATA")
    print("Name: {:s}".format(product.name))
    print("Price: {:.2f}".format(product.price))
    print("Discount percent: {:d}%".format(product.discountPercent))
    print("Discount amount: {:.2f}".format(product.getDiscountAmount()))
    print("Discount price: {:.2f}".format(product.getDiscountPrice()))

def main():
    print("The Product Viewer Program")

    # 1. Create the tuple of Product objects
    products = (Product("Stanley 24 OUnce Wood Hammer", 12.99, 62),
                Product("National Hardware 3/4", 5.06, 0),
                Product("Economy Duct Tape 60 yd, Silver", 7.24, 0))

    # 2. Display the numbered list of product by passing the tuple to the show_products()function
    # defined earlier in the module
    show_products(products)

    # 3. Prompt the user to enter a number that corresponds with a product.
    while True:
        number = int(input("Enter product number: "))
        print()
    # 4. Get the corresponding Product object from the tuple of the Product objects
        product = products[number-1]

    # 5. Display data of the product object by passing the object to the show_product()
        show_product(product)

        choice = input("View another product? (y/n): ")
        print()

        if choice.lower() != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()