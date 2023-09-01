#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5, 23, 21, 14, 23, 12, 4, 12, 22, 22, 34, 12]
previousMonthSalary = 0 # initializing the previous month salary as 0

#  loop that iterates over each month and the corresponding number of phones sold in the monthlySalesList
for month, phoneCount in enumerate(monthlySalesList): #The enumerate function is used to get both the index of the month and the corresponding phone count.
    basePay = 10000
    bonusPerFivePhones = 5000
    bonusPerExtraPhone = 1100

    totalBonus = (phoneCount // 5) * bonusPerFivePhones #calculates bonus for every five phones sold

    if phoneCount > 5:
        totalBonus += (phoneCount - 5) * bonusPerExtraPhone #calculates bonus after the first 5 phones and add to the totalbonus

    currentMonthSalary = basePay + totalBonus # calculating the current month salary before adding the additional bonus

    print(f"This month's salary before additional bonus: {currentMonthSalary}")

    if previousMonthSalary > 20000 and phoneCount >= 20: #checking the condition for additional bonus
        currentMonthSalary += 5000 # adding the additional bonus to current month salary
        print(f"This month's salary after additional bonus: {currentMonthSalary}")

    previousMonthSalary = currentMonthSalary
    
    print(f"monthly salary of a salesman:{previousMonthSalary}")