## DAY--3
#IF/ELSE conditions used method:

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before yuu can ride.")

#--odd/Even exercise

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is a Even number.")
else:
    print("This is a Odd number.")



## DAY--3
## BMI--Calculator 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi <25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi <30:
    print(f"Your bmi is {bmi}, you are slightly overweight.")
elif bmi <35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")


## Interactive coding exercise (leap-year)

year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year")

## PIZZA--ORDER-PRACTICE


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")



##--LOVE--Calculator exercise.

print("Welcome to the Loving Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
seocnd_digit = l + o + v + e

score = int(str(first_digit) + str(seocnd_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >=40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")


