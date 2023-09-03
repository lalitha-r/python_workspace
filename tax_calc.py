total_income = float(input("Enter total income: "))
deductions = float(input("Enter total deductions: "))

taxable_income = total_income - deductions

if taxable_income <= 250000:
    tax = 0
elif 250000 < taxable_income <= 500000:
    tax = 0.05 * (taxable_income - 250000)
elif 50000 < taxable_income <= 1000000:
    tax = 0.20 * (taxable_income - 500000) + 12500
else:
    tax = 0.30 * (taxable_income - 1000000) + 112500

health_education_cess = 0.04 * tax
total_tax = tax + health_education_cess

print("Income Tax: Rs.", total_tax)