#age input from user
age = int(input("Please enter your age: "))

# check if variable age is greater than 100
if(age>100): 
    print("Sorry, you're dead.")

#check if over or equal to 65 (but less than 101 because of statement above)
elif(age>=65):
    print("Enjoy your retirement!")

#check if greater or equal on 40 (but less than 65 based on above)
elif(age>=40):
    print("You're over the hill.")

#Now check if less than 13
elif(age<13):
    print("You qualify for the kiddie discount.")

#Check if it is exactly 21 with ==
elif(age == 21):
    print("Congrats on your 21st!")

# for all others (equal and over 13, less 40, not 21)
else:
    print("Age is but a number.")

