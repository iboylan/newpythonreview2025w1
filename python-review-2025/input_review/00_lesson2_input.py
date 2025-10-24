# Goal: show how input works, type conversion, and basic math output.


print("Welcome! We'll do some math.\n")

# Get two numbers from the user and ask for their name to personalize the experience
name = input("What's your name?   ")
print(f"Your name is: {name}.")
num1 = input("Number 1?   ")
print(f"{name} set number 1 to {num1}.")
num2 = input("Number 2?   ")
print(f"{name} set number 2 to {num2}.")
operationtype = str(input("Which operation would you like to perform? Ensure it's written in lowercase and spelled correctly with no spaces. (Add, subtract, multiply, divide, or exponent)   "))
print(f"{operationtype}")
if operationtype != "multiply" or "add" or "subtract" or "divide" or "exponent":
    while operationtype != "multiply" or "add" or "subtract" or "divide" or "exponent": operationtype = str(input("That's not a valid operation. Ensure it's written in lowercase and spelled correctly with no spaces. Which operation would you like to perform? (Add, subtract, multiply, divide, or exponent)   "))
    else:
        print(f"{name} set operation to {operationtype}.")










# Student  notes (say out loud):

        # “input() is always text. That’s why we convert.”

        # “float() lets us do decimal math; int() is only whole numbers.”

        # “Division by zero crashes programs—so we check first.”

        # “{value:.2f} rounds to 2 decimals right in the f-string.”

# Common pitfalls to point out:

        # Forgetting to cast → "3" + "4" becomes "34" (string concatenation)

        # Using ^ for exponent (Python uses **)

        # Missing quotes around string literals

        # Forgetting the f in f-strings