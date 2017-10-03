#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:57:08 2017

@author: ujjwal
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

print "Welcome to Ujjwal's Calculator"
Principal = input("Principal: ")
Coupon = input("Coupon: ")
Yield = input("Yield: ")
Tenor = input("Tenor: ")

print "\nPrice: ", bondPrice(Principal, Coupon, Yield, Tenor)