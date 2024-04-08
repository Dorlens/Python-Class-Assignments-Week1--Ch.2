#Dorlens Janvier chapter 2 question 1


import math 
# Declare variables and made them constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0


 #Prompt the user
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

#calculated the income tax 
taxableIncome = grossIncome - STANDARD_DEDUCTION -  DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

rounded_Income_Tax = round(incomeTax,2)
#Display the income tax 
print("The income tax is $" + str(rounded_Income_Tax))