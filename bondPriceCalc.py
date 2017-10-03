#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
A recursive function to calculate bond price.
"""


def bondPrice(Principal, Coupon, Yield, Tenor):
    
    #assume interest paid annually for now
    c = Coupon
    p = Principal
    r = Yield
    n = Tenor
    
    price = p
    
    #using recursion
    if n >0:
        price = bondPrice((price + c)/(1 + r), c, r, n - 1)
    
    return price

print "Provide inputs to calculate a bond price"

Principal = input("Principal: ")
Coupon = input("Coupon: ")
Yield = input("Yield: ")
Tenor = input("Tenor: ")

print "\nPrice: ", bondPrice(Principal, Coupon, Yield, Tenor)
