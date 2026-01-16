""" "Task 1: Zero-shot Prompt - Fibonacci Series Generator"
# Generate a Python function that takes an integer N as input and prints the first N Fibonacci numbers starting from 0
def print_fibonacci(N):
    a, b = 0, 1
    for _ in range(N):
        print(a, end=' ')
        a, b = b, a + b
    print()  # for a new line after printing the Fibonacci numbers
# Example usage:
n = int(input("Enter the number of Fibonacci numbers to print: "))
print_fibonacci(n)  # This will print the first n Fibonacci numbers" """

""" "Task 2: One-shot Prompt - List Reversal Function"
# Write a Python function that takes a list as input and returns the reversed list
# Example: input = [1, 2, 3], output = [3, 2, 1]
def reverse_list(input_list):
    return input_list[::-1]
# Example usage:
example_list = list(map(int, input("Original List: ").split()))
print("Reversed list:", reverse_list(example_list)) """


""" "Task 3: Few-shot Prompt - String Pattern Matching"
# Write a Python function is_valid(s) that returns True if a string starts with a capital letter and ends with a period, otherwise False
# Example: "Hello world." → True
# Example: "hello world." → False
# Example: "Hello world" → False
def is_valid(s):
    return s[0].isupper() and s.endswith('.')
# Example usage:
test_string = input("Enter a string: ")
print(is_valid(test_string))  # This will print True or False based on the input string """


""" "Task 4: Zero-shot vs Few-shot - Email Validator (Zero-shot Prompt)"
# Write a Python function to validate whether an email address is valid or not
def is_valid_email(email):
    import re
    return re.match(pattern, email) is not None
# Example usage:
email_input = input("Enter an email address: ")
if is_valid_email(email_input):
    print("Valid email address")
else:
    print("Invalid email address") """


""" "Task 4: Zero-shot vs Few-shot - Email Validator (Few-shot Prompt)"
# Write a Python function is_valid_email(email) that returns True for valid emails and False otherwise
# Example: "user@gmail.com" → True
# Example: "user123@yahoo.in" → True
# Example: "usergmail.com" → False
# Example: "user@.com" → False
def is_valid_email(email):
    import re

    return re.match(pattern, email) is not None
# Example usage:
email_input = input("Enter an email address: ")
print(is_valid_email(email_input))  # This will print True or False based on the email validity """


""" "Task 5: Prompt Tuning - Summing Digits of a Number (Genereic Task Prompt)"
# Write a Python function that returns the sum of digits of a given number
def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total
# Example usage:
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))  # This will print the sum of the digits of the number """



"Task 5: Prompt Tuning - Summing Digits of a Number (Task + Input/Output example)"
# Write a Python function sum_of_digits(n) that returns the sum of all digits in a number
# Example: input = 123, output = 6
def sum_of_digits_tuned(n):
    return sum(int(digit) for digit in str(n))
# Example usage:
num_tuned = int(input("Enter a number: "))
print("Sum of digits (tuned):", sum_of_digits_tuned(num_tuned))  # This will print the sum of the digits of the number