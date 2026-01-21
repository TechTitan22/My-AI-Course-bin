# Question 1 
# Write a program that converts a temperature from Celsius to Fahrenheit. 
# (Formula: Fahrenheit = (Celsius * 9/5) + 32)

celsius = float(input("Enter the Temperature in Celsius: "))
Fahrenheit = (celsius * 1.8) + 32
print("temperature in Fahrenheit is ", Fahrenheit)


# Question 2 
# Calculate Area of a Rectangle 

L = int(input("Enter the Length of the Rectangle:"))
W = int(input("Enter the width of the Rectangle:"))

Area = L * W 
print("Area of the Rectangle is ", Area)


# Question 3 
# Calculate Compound Interest Use the formula: CI = P * (1 + R/100)**T - P 
# Where P = principal, R = rate, T = time 

print("Require things to find the Compound interest")
P = int(input("Enter the Principal :"))     # Principal -> initial investment 
R = int(input("Enter the Rate :"))
T = float(input("Enter the Time:"))

CI = P * (1 + R/100)**T - P 
print("Compound Interest is ", CI)


# Question 4 
# Perimeter of a Rectangle - Take length and width as input and calculate the perimeter.

L = int(input("Enter the Length of Perimeter : "))
W = int(input("Enter the width of the Perimeter : "))

# Perimeter's Formula 
P = 2 * (L + W)
print("Perimeter of the Rectangle is ", P)


# Question 5 
# Average of Three Numbers - Input three numbers and print their average. 

print("Enter the three numbers : ")
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))

s = n1 + n2 + n3
print("Sum of Three Numbers = ", s)
Avg = s/3
print("Average of Three Numbers = ", Avg)


# Question 6 
# Square and Cube of a Number - Ask the user for a number and display its square and cube.

num = int(input("Enter Number: "))
Square = num**2
Cube = num**3
print(f'Square of the {num} is',Square)
print(f'Cube of the {num} is',Cube)


# Question 7
# Distribute Items Equally - You have n candies and k students.Write a program to find: 
# how many candies each student gets 
# how many are left 

n = int(input("Enter the Number of Candies: "))
k = int(input("Enter the Number of Students: "))

student_gets = n // k 
print("Number of Candies each Student gets", student_gets)
candies_left = n % k 
print("Number of Candies Left ", candies_left)


# Question 8
# Calculate Profit or Loss Input cost price and selling price. Display either: 
# Profit and amount, or 
# Loss and amount, or 
# No Profit No Loss

Cost_Price = int(input("Enter the Cost Price of the Product: "))
Selling_Price = int(input("Enter the Selling Price of the Product: "))

profit = (Selling_Price - Cost_Price)
loose = (Cost_Price - Selling_Price)
if Selling_Price > Cost_Price: 
   print(f'Profit: {profit} and Amount: {Selling_Price}')
else:
   print(f'Loose: {loose} and Amount: {Selling_Price}')


# Question 9
# Total Marks and Percentage Input marks of 5 subjects. Print: 
#  Total marks 
#  Percentage 
#  Average 

print("Enter the Marks of 5 subjects: ")
Total_Marks = 0
for i in range(1,6): 
  marks = int(input(f'Subject_{i} : '))
  Total_Marks += marks
print("Total Marks: ",Total_Marks)
Per = (Total_Marks/500)*100 
print(f'Percentage: {Per}%')
Avg = (Total_Marks/5)
print("Average: ",Avg)


# Question 10 
# Salary Calculator Input basic salary. Calculate: 
#  HRA = 20% of basic 
#  DA = 15% of basic 
#  Total Salary = Basic + HRA + DA 

Basic = int(input("Enter the basic salary: ").replace(',',''))
HRA = 0.2 * Basic
DA = 0.15 * Basic

Total_Salary = Basic + HRA + DA
print(f'HRA: {HRA}')
print(f'DA: {DA}')
print(f'Total Salary: {Total_Salary}')


# Question 11
# Age in Months and Days Input your age in years. Calculate and print age in: 
#  Months 
#  Days (approximate)

age_years = int(input("Enter the Age in Years: "))

age_months = age_years * 12
age_days = age_years * 365 

print("Age in Months: ", age_months)
print("Age in Days (Approximately): ", age_days)


# Question 12 
# Currency Converter (USD to PKR) Input amount in USD. Convert using a fixed exchange rate.

exchange_rate = 280
USD_amount = float(input("Enter the Amount in USD: ").replace('$',''))
PKR_amount = USD_amount * exchange_rate

print(f'USD Amount: {USD_amount} convert into PKR Amount: {PKR_amount}')


# Question 13 
# Sum of First N Natural Numbers Input a number n, calculate sum of first n natural numbers. 
# Formula: sum = n * (n + 1) / 2

n = int(input("Enter the Number n: "))
sum = n * (n + 1) / 2 

print(f'The Sum of all {n} Natural Numbers are ',sum)


# Question 14 
#Percentage of Correct Answers 
#Input total questions and correct answers, and calculate the percentage score.

total_questions = int(input("Enter total number of questions: "))
correct_answers = int(input("Enter number of correct answers: "))

# Calculate percentages
percentage_correct = (correct_answers / total_questions) * 100
percentage_wrong = 100 - percentage_correct

# Display results
print(f"\nTotal Questions: {total_questions}")
print(f"Correct Answers: {correct_answers}")
print(f"Incorrect Answers: {total_questions - correct_answers}")
print(f"Percentage of Correct Answers: {percentage_correct:.2f}%")
print(f"Percentage of Incorrect Answers: {percentage_wrong:.2f}%")


# Question 15 
# Speed, Distance, and Time Input distance and time, and calculate speed.

distance =int(input("Enter the Distance: "))
time = int(input("Enter the Time: "))

Speed = distance/time 

print(f"Speed = {Speed:.2f} km/h")



# Question 16 
# Calculate Body Mass Index (BMI) Input weight (kg) and height (m), then calculate: 
# BMI = weight / (height ** 2)

weight =float(input("Enter Weight (kg)"))           #solve this in feet and inches also 
height =float(input("Enter the Height (m) "))

BMI = weight / (height ** 2)

print(f'According to the Weight {weight} kg and Height {height} m. The BMI is : {BMI:.2f}')

# BMI Calculator 
if BMI < 18.5 :
    print("You are Under_Weight")
elif 18.5 <= BMI < 24.9:
    print("You have a Normal Weight")
elif 25 <= BMI < 29.9:
    print("You have a Over_Weight")
else: 
    print("You are Obese")



# Question 17
# Convert Minutes to Hours and Minutes Input number of minutes and convert to hours and remaining minutes. 
# Example: 130 minutes → 2 hours 10 minutes

min = int(input("Enter the Minutes in Numbers: "))
hour = min // 60            # hour = min/60  
remaining_min = min%60
print(f'{hour} Hour(s) {remaining_min} Minute(s)')    #### Search (s) 
