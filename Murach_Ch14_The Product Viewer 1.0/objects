#******************************************************************************
# Author:           Joel Murach
# Date:             02.15.2022
# Description:      An example from Murach's Python textbook
#                   This module contains a class named Product. This code defines a constructor that initializes
#                   the attributes that store the name, price, and discount percent for the object. Then, it defines
#                   two methods that get the discount amount and price for the object.
# Sources:          Murach's Python Programming - Beginner
#                   Chapter 14_ How to define and use your own classes
#                   Example: The Product Viewer program 1.0
#******************************************************************************


class Product:
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()
