income_slabs = [250000, 500000, 1000000]# slab amount are defined in array list
tax_rates = [0.05, 0.20, 0.30]# tax percentage are defined in array list

# get total income as input from the user
total_income = float(input("Enter total income: "))

# get deductions as input from the user
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
            taxable_amount = income_slabs[i + 1] - income_slabs[i]
        else:
            taxable_amount = taxable_income - income_slabs[i]
        
        tax_in_slab = taxable_amount * tax_rates[i]
        cumulative_tax = cumulative_tax + tax_in_slab
    else:
        break

# Add 4% health and education cess
cess = 0.04 * cumulative_tax

# Calculate total tax
total_tax = cumulative_tax + cess

# Display the calculated tax
print("Income Tax: Rs.", total_tax)

# output
#Enter total income: 300000
#Enter deductions: 150000
#Income Tax: Rs. 0.0
#logesh@Logeshs-MacBook-Pro python_workspace %  cd /Users/logesh/python_workspace ; /usr/bin/env /usr/local/bin/python3 /Users/logesh/.vscode/extensio
#ns/ms-python.python-2023.14.0/pythonFiles/lib/python/debugpy/adapter/../../debugpy/launcher 53058 -- /Users/logesh/python_workspace/tax_array.py 
#Enter total income: 600000
#Enter deductions: 150000
#Income Tax: Rs. 13000.0

