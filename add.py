def calculate_sum(a, b):
    sum_result = a + b
    return sum_result

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the calculate_sum function
result = calculate_sum(num1, num2)

# Print the result
print("The sum of", num1, "and", num2, "is:", result)
