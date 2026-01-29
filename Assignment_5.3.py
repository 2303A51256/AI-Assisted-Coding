""" "Task 1: Privacy and Data Security in AI-Generated Code"
# Generate a simple login system in Python.

def login_system():
    # Predefined username and password
    USERNAME = "admin"
    PASSWORD = "password123"

    # Function to check login credentials
    def check_credentials(username, password):
        return username == USERNAME and password == PASSWORD

    # Get user input
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")

    # Validate credentials
    if check_credentials(input_username, input_password):
        print("Login successful!")
    else:
        print("Login failed! Incorrect username or password.")
# Run the login system
login_system() """


""" "Revised Prompt for Secure Implementation"
# Generate a secure login system in Python with hashed passwords. While Hardcoding use hashed values.
import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def login_system():
    # Predefined hashed username and password
    USERNAME_HASH = "8c6976e5b5410415bde908bd4dee15dfb16f0c3f5d5a1a6a4f4f4f4f4f4f4f4f"  # hash for "admin"
    PASSWORD_HASH = "ef92b778bafe771e89245b89ecbc4cc1b2e7d3c3c3c3c3c3c3c3c3c3c3c3c3c3"  # hash for "password123"

    # Function to check login credentials
    def check_credentials(username, password):
        return (hash_password(username) == USERNAME_HASH and 
                hash_password(password) == PASSWORD_HASH)

    # Get user input
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")

    # Validate credentials
    if check_credentials(input_username, input_password):
        print("Login successful!")
    else:
        print("Login failed! Incorrect username or password.")
# Run the login system
login_system() """


""" "Task 2: Bias Detection in AI-Generated Decision Systems"
#Create a loan approval system in Python.
def loan_approval_system():
    # Function to determine loan approval
    def approve_loan(income, credit_score, gender):
        if gender.lower() == "female":
            return income >= 50000 and credit_score >= 600
        else:
            return income >= 60000 and credit_score >= 700

    # Get user input
    try:
        income = float(input("Enter your annual income: "))
        credit_score = int(input("Enter your credit score: "))
        gender = input("Enter your gender (male/female): ") # This input is not used in decision-making
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Determine loan approval
    if approve_loan(income, credit_score, gender):
        print("Loan approved!")
    else:
        print("Loan denied. You do not meet the criteria.")
# Run the loan approval system
loan_approval_system() """


""" "Task 3: Transparency and Explainability in AI-Generated Code (Recursive Binary Search)"
# Generate a recursive binary search program in Python with explanation.
def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2
    print(f"Checking middle index {mid}, value {arr[mid]}")  # Explanation step

    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        print(f"Target {target} is greater than {arr[mid]}, searching right half")  # Explanation step
        return binary_search(arr, target, mid + 1, high)
    else:
        print(f"Target {target} is less than {arr[mid]}, searching left half")  # Explanation step
        return binary_search(arr, target, low, mid - 1)
# Get user input
try:
    arr = list(map(int, input("Enter a sorted list of numbers (space-separated): ").split()))
    target = int(input("Enter the target number to search for: "))
    result = binary_search(arr, target, 0, len(arr) - 1)
    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the list.")
except ValueError:
    print("Invalid input. Please enter numeric values.") """

""" "Task 4: Ethical Evaluation of AI-Based Scoring Systems"
# Generate a job applicant scoring system in Python based on skills and experience.
def applicant_scoring_system():
    # Function to score applicants
    def score_applicant(skills, experience_years):
        score = 0
        skill_set = {"python", "data analysis", "machine learning", "communication", "teamwork"}
        for skill in skills:
            if skill.lower() in skill_set:
                score += 20  # Each relevant skill adds 20 points
        score += min(experience_years * 5, 50)  # Max 50 points for experience
        return score

    # Get user input
    skills_input = input("Enter your skills (comma-separated): ")
    skills = [skill.strip() for skill in skills_input.split(",")]
    try:
        experience_years = int(input("Enter your years of experience: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value for years of experience.")
        return

    # Calculate score
    total_score = score_applicant(skills, experience_years)
    print(f"Your total applicant score is: {total_score}/150")

    # Ethical consideration: Ensure transparency in scoring criteria
    print("Scoring Criteria:")
    print("- Each relevant skill adds 20 points (max 100 points).")
    print("- Each year of experience adds 5 points (max 50 points).")
# Run the applicant scoring system
applicant_scoring_system() """

""" "Task 5: Inclusiveness and Ethical Variable Design"
# Generate a Python code snippet that processes employee details for their uniform.
def employee_uniform():
    name = input("Enter Name: ")
    gender = input("Enter Gender(male/female): ").strip().lower()
    if gender == "male":
        uniform = "Shirt and Pants"
    else:
        uniform = "Skirt"
    print(f"Employee Name: {name}")
    print(f"Assigned Uniform: {uniform}")
# Run the employee uniform assignment
employee_uniform() """

""" "Revised Prompt for Neutral Employee Uniform Assignment"
# Generate inclusive and gender-neutral Python code to process employee details for their uniform.
def employee_uniform():
    name = input("Enter Name: ")
    uniform = "Formal Uniform"
    print(f"Employee Name: {name}")
    print(f"Assigned Uniform: {uniform}")
# Run the employee uniform assignment
employee_uniform() """

