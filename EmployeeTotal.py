#Dorlens Janvier chapter 2 question 10

# I declared the variables and prompt the user 
hourlyWage = float(input("Enter your hourly wage:"))
totalRegularHours = int(input("Enter your total regular hours:"))
totalOverTimeHours = int(input("Enter your total overtime hours:"))

# I calculated the the regular pay and the overtime pay
regularPay = hourlyWage * totalRegularHours
overTimePay = totalOverTimeHours * 1.5 * hourlyWage
totalWeeklyPay = regularPay + overTimePay

# I printed out the employee weekly pay
print("The employee weekly pay is:",totalWeeklyPay)