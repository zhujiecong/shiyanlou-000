#!/usr/bin/env python3
import sys
salary = int(sys.argv[1])
#print ("salary = ",salary)
taxable_income = salary -3500
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

print(format(tax , ".2f"))
