#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ujjwal

A recursive function to calculate bond price

Units:
Principal and coupon in dollars
Yield in %
Tenor in years
"""


def bondPrice(Principal, Coupon, Yield, Tenor):
    
    #assume interest paid annually for now
    c = Coupon
    p = Principal
    r = Yield
    n = Tenor
    
    price = p
    
    #using recursion
    if n > 0:
        price = bondPrice((price + c)/(1 + r), c, r, n - 1)
    
    return price

print("Provide inputs to calculate a bond price")

Principal = float(input("Principal: "))
Coupon = float(input("Coupon: "))
Yield = float(input("Yield: "))/100
Tenor = float(input("Tenor: "))

print("Price: ", bondPrice(Principal, Coupon, Yield, Tenor))
