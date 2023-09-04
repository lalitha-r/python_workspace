income_slabs = [250000, 500000, 1000000]
tax_rates = [0.05, 0.20, 0.30]

# Input total income
total_income = float(input("Enter total income: "))

# Input deductions
deductions = float(input("Enter deductions: "))

# Calculate taxable income
taxable_income = total_income - deductions

# Initialize tax and cumulative tax
tax = 0
cumulative_tax = 0

# Iterate through income slabs and calculate tax
for i in range(len(income_slabs)):
    if taxable_income > income_slabs[i]:
        if i < len(tax_rates) - 1:
            taxable_amount_in_slab = income_slabs[i + 1] - income_slabs[i]
        else:
            taxable_amount_in_slab = taxable_income - income_slabs[i]
        
        tax_in_slab = taxable_amount_in_slab * tax_rates[i]
        cumulative_tax += tax_in_slab
    else:
        break

# Add 4% health and education cess
cess = 0.04 * cumulative_tax

# Calculate total tax
total_tax = cumulative_tax + cess

# Display the calculated tax
print("Income Tax: Rs.", total_tax)