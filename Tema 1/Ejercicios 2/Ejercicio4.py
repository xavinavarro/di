#!/usr/bin/env python


hamburger=0
water=0
salad=0

order=input ('El pedido es: \n')

s = 'hamburger: '+str(order.count('hamburger'))'\n'+'water: '+str(order.count('water'))'\n'+'salad: '+str(order.count('salad'))
print(s)