print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
people=int(input("How many people to split the bill?"))
tip=int(input("How much tip would you like to give? 10%, 12%, or 15%? "))
each_person=(bill+(bill*(tip/100)))/people
final_each_person=round(each_person,2)
print(f"Each person should pay: ${final_each_person}")