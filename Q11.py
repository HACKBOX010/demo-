# Write a Python Program to Check if a Number is Positive, Negative or Zero.
# Function to check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
number = float(input("Enter a number: "))
result = check_number(number)
print(f"The number is {result}.")
