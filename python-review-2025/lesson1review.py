#Part one: For each line of code below, write what type of variable is being stored (string, integer, or float). Write your answer as a comment next to each line of code.

first_name = "oobygoobert" # for example: this is a string
food = "pizza"
email = "Bro123@fake.com"
age = 25
quantity = 3
price = 10.99
gpa = 3.2
distance = 5.5

#Part 2 – Predict the Output

#Without running the code, predict what each line will print:
print(f"Hello {first_name}") # for example: Hello Bro
print(f"You like {food}") # for example: You like pizza
print(f"Your email is: {email}")
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance} km")


# Part 3 – Fix the Errors

# The following code has two mistakes.
# Find and fix them so it runs correctly.

name = "Bro"
food = "pizza"
print(f"Hello {name}")
print(f"You like {food}")

# Missing quotes and wrong variable name
favorite_food = "pizza"
print(f"You like {favorite_food}")

# Wrong f-string format
age = 17
print(f"You are {age} years old")

# Mismatched parentheses
price = 12.99
print(f"The total price is ${price}")
      

# Variable name spelled incorrectly
name = "Bro"
print("Hello ",{name})

# Using + instead of commas
name = "Bro"
print("Hello ",{name})

# Mixing single and double quotes incorrectly
email = "Bro123@fake.com"
print(f"Your email is: {email}")

# Forgot to include the f before the string
age = 21
print(f"You are {age} years old")

# Trying to use a number as a variable
cool = "NO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print(f"Am I cool? {cool}")

# Missing curly braces
quantity = 3
print(f"You are buying {quantity} items")

# Using a reserved keyword
classcurrent = "ECS"
print(f"You are in {classcurrent}")



# Part 4 – Create Your Own

# Write a short Python program that:

# Creates at least three variables (a string, an integer, and a float)

# Prints a formatted message using f-strings that combines all three.

game = "Splatoon 3"
copyno = 11.96
year = 2022
print(f"My favorite game is {game}, released in {year}, with {copyno} million copies sold!")

