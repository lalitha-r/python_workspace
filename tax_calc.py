total_income = float(input("Enter total income: "))#getting the income as a input from user as float
deductions = float(input("Enter total deductions: "))#getting the deduction amount from the user

taxable_income = total_income - deductions # calculating the taxable income 

if taxable_income <= 250000: # no tax if the income is less than 2.5 lakhs
    tax = 0
elif 250000 < taxable_income <= 500000: # calculating tax for slab 1 
    tax = 0.05 * (taxable_income - 250000)
elif 50000 < taxable_income <= 1000000: # calculating the tax for slab 2
    tax = 0.20 * (taxable_income - 500000) + 12500
else:
    tax = 0.30 * (taxable_income - 1000000) + 112500 # calculating the tax fro slab 3

health_education_cess = 0.04 * tax # calculating  health cess
total_tax = tax + health_education_cess

print("Income Tax: Rs.", total_tax)