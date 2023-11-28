#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.
#if cummulative  bonus is greater thaan or equal to one lakh then the base salary increase by 5%
monthlySalesList = [5, 23, 21, 14, 23, 12, 4, 12, 22, 22, 34, 12]
previousMonthSalary = 0  # initializing the previous month salary as 0

# Initialize variables for base salary and cumulative bonus
basePay = 10000
cumulativeBonus = 0

# Loop that iterates over each month and the corresponding number of phones sold in the monthlySalesList
for month, phoneCount in enumerate(monthlySalesList):  # The enumerate function is used to get both the index of the month and the corresponding phone count.
    bonusPerFivePhones = 5000
    bonusPerExtraPhone = 1100

    totalBonus = (phoneCount // 5) * bonusPerFivePhones  # calculates bonus for every five phones sold

    if phoneCount > 5:
        totalBonus += (phoneCount - 5) * bonusPerExtraPhone  # calculates bonus after the first 5 phones and add to the total bonus

    currentMonthSalary = basePay + totalBonus  # calculating the current month salary before adding the additional bonus

    if previousMonthSalary > 20000 and phoneCount >= 20:  # checking the condition for additional bonus
        currentMonthSalary += 5000  # adding the additional bonus to current month salary

    cumulativeBonus += totalBonus  # Update cumulative bonus

    # Check if cumulative bonus is greater than or equal to one lakh
    if cumulativeBonus >= 100000:
        basePay += basePay * 0.05  # Increase base salary by 5%

    previousMonthSalary = currentMonthSalary

    print(f"Monthly salary of a salesman for month {month + 1}: {previousMonthSalary}")

print(f"Final base salary after cumulative bonus increase: {basePay}")


# Monthly salary of a salesman for month 1: 15000
# Monthly salary of a salesman for month 2: 49800
# Monthly salary of a salesman for month 3: 52600
# Monthly salary of a salesman for month 4: 29900
# Monthly salary of a salesman for month 5: 55300.0
# Monthly salary of a salesman for month 6: 28725.0
# Monthly salary of a salesman for month 7: 11576.25
# Monthly salary of a salesman for month 8: 29855.0625
# Monthly salary of a salesman for month 9: 56462.815625
# Monthly salary of a salesman for month 10: 57100.95640625
# Monthly salary of a salesman for month 11: 80971.0042265625
# Monthly salary of a salesman for month 12: 32474.554437890627
