"""json module is imported to work with json data"""
import json

# Read the employee personal details from the JSON file
with open("employee_personal_details.json", "r", encoding="utf-8") as file:
    employee_details = json.load(file)

# Function to fix salary hike for a business unit
def fix_salary_hike(business_unit, percentage):
    """this function deals with fike salary hike"""
    for employee in employee_details:
        if employee["Business Unit"] == business_unit:
            salary = employee["Salary"]
            new_salary = salary + (salary * (percentage / 100))
            employee["Salary"] = new_salary

# Example usage: fix a salary hike for a business unit
fix_salary_hike("Sales", 10)

# Write the updated employee details to the JSON file
with open("employee_personal_details.json", "w", encoding="utf-8") as file:
    json.dump(employee_details, file, indent=4)

print("Salary hike applied and employee details updated successfully!")
