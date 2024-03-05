"""This generates a random fake data """
import json
from faker import Faker

fake = Faker()

employee_details = []

# Generate 50-100 records
num_records = fake.random_int(min=50, max=100)
for _ in range(num_records):
    emp_id = fake.unique.random_number(digits=6)
    emp_name = fake.name()
    emp_email = fake.email()
    business_unit = fake.company_suffix()
    salary = fake.random_int(min=30000, max=100000)

    employee_details.append({
        "EMP ID": emp_id,
        "EMP NAME": emp_name,
        "EMP EMAIL": emp_email,
        "Business Unit": business_unit,
        "Salary": salary
    })

with open("employee_personal_details.json", "w",encoding="utf-8") as file:
    json.dump(employee_details, file, indent=4)
print("JSON file 'employee_personal_details.json' created successfully!")
