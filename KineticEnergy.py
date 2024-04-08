# Dorlens Jnavier chapter 2 question 6


# i declared and variables and also prompt the user 
objectsMass = float(input("Enter the objects mass in kilograms:"))
velocity =  float(input("Enter the velocity in meters per second:"))

# I calculated the momentum 
momentum = objectsMass * velocity 

kineticEnergy = 0.5 * objectsMass * velocity**2

# I printed the calculated momentum and kinetic energy
print("The kinetic energy is:" ,kineticEnergy)
print ("the momentum is: " , momentum )