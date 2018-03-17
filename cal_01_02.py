#!/usr/bin/env python3
import sys

#config
premium_rate  = 0.165  
Threshold = 3500
 

def pay(salary):
    taxable_income = salary*(1- premium_rate) -3500
    if taxable_income <= 1500:
        tax = taxable_income * 0.03
    elif 1500 < taxable_income <= 4500:
        tax = taxable_income * 0.10 - 105
    elif 4500 < taxable_income <= 9000:
        tax = taxable_income * 0.20 - 555
    elif 9000 < taxable_income <= 35000:
        tax = taxable_income * 0.25 - 1005
    elif 35000 < taxable_income <= 55000:
        tax = taxable_income * 0.30 - 2755
    elif 55000 < taxable_income <= 80000:
        tax = taxable_income * 0.35 - 5505
    elif 80000 < taxable_income:
        tax = taxable_income * 0.45 - 13505
    return format(salary*(1- premium_rate) - tax,".2f")


#salary = int(sys.argv[1])
#print(salary) 
#salary_d = dict()
pay_d = dict()
#print(sys.argv[1])

for arg in sys.argv[1:]:
    try:
        pay_d[int(arg.split(':')[0])] = pay(int(arg.split(':')[1]))
    except ValueError:
        print("Parameter Error")

for key,value in pay_d.items():
    print(str(key)+':'+str(value))
#print(format(pay(salary), ".2f"))
