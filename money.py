#initializing the total money and asking count as 0
total_money = 0
ask_count = 0

for i in range(5):  # Maximum of 5 times
    money_given = int(input("Enter the money  parents gave : "))
    #counting how many times we are asking for to the parents
    
    ask_count += 1
    #if the money given by parents is greater than rs 10, add it to the total money
    if money_given > 10:
        total_money += money_given
        print(f"Thank you. i have received a total of Rs {total_money} so far.")
        #checking whether the total money reached to rs1000
        if total_money >= 1000:
            break
    else:
        print("This amount is not added towards the Rs 1000.")
        continue
    

print(f"Total amount received: Rs {total_money}")
print(f"I ask my parents {ask_count} times to get this money.")