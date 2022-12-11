#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator!!!")
total_bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
print(total_bill)
print(tip)
print(people)
total_tip = total_bill * (tip / 100)
print(total_tip)
per_person_bill = (total_bill + total_tip) / people
#print(round(per_person_bill, 2))
per_person_bill = "{:.2f}".format(per_person_bill)
print("Each person should pay = $",per_person_bill)
