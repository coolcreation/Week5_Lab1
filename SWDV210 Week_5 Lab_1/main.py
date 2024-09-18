#!/usr/bin/env python3

# Jeff Bohn
# 9/17/2024
# main.py
# SWDV210 - Week_5-Lab_1
# Chapter 9 - Working with Numbers

from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc
lc.setlocale(lc.LC_ALL, "us") 


# display a title
print("The Invoice program\n")


# add a function to validate user input
def validation():
    while True:
        try:
            value = float(input("Enter order total: "))
            value = Decimal(value)
            #print("try")
            return value 
        except Exception as e:
            #print("Enter a number only: ")
            print(Exception, e)


# add a function to calculate shipping cost
def calcShippingCost(cost):
    cost = Decimal(cost) * Decimal(".085")
    cost = cost.quantize(Decimal("1.00"), ROUND_HALF_UP)
    return cost


def main():

    choice = "y"
    while choice == "y":
        
        # get the user entry
        order_total = validation()
        order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
        print()               

        # determine the discount percent
        if order_total > 0 and order_total < 100:
            discount_percent = Decimal("0")
        elif order_total >= 100 and order_total < 250:
            discount_percent = Decimal(".1")
        elif order_total >= 250:
            discount_percent = Decimal(".2")

        # calculate the results
        discount = order_total * discount_percent
        discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
        subtotal = order_total - discount
        shipping_cost = calcShippingCost(subtotal)
        tax_percent = Decimal(".05")
        sales_tax = subtotal * tax_percent 
        sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)                                 
        invoice_total = (subtotal + sales_tax) + shipping_cost

        # display the results
        sp = 20
        print(f"Order total:        {lc.currency(order_total, grouping=True):>{sp}}")   #lc.currency(order_total, grouping=True) 
        print(f"Discount amount:    {discount:{sp}}")
        print(f"Subtotal:           {subtotal:{sp}}")
        print(f"Shipping cost:      {shipping_cost:{sp}}")
        print(f"Sales tax:          {sales_tax:{sp}}")
        print(f"Invoice total:      {lc.currency(invoice_total, grouping=True):>{sp}}")
        print()

        choice = input("Continue? (y/n): ")    
        print()
        
    print("Bye!")

if __name__ == "__main__":
    main()