import csv
from faker import Faker
import random
from datetime import datetime, timedelta


fake = Faker()

# take random hiring dates
def generate_hiring_date():
    start_date = datetime(2010, 1, 1)
    end_date = datetime.now()
    hiring_date = fake.date_time_between(start_date=start_date, end_date=end_date)
    return hiring_date.strftime('%Y-%m-%d')

# random departments
def generate_department():
    departments = ['Finance', 'Human Resources', 'Marketing', 'Operations', 'Information Technology']
    return random.choice(departments)

# random birthdays
def generate_birthday():
    max_age = 65
    birth_date = fake.date_of_birth(tzinfo=None, minimum_age=max_age)
    return birth_date.strftime('%Y-%m-%d')

# Function to generate employee data and write to CSV file
def generate_data(num_employees):
    with open('database.csv', mode='w', newline='') as file:
        fieldnames = ['Name', 'Hiring Date', 'Department', 'Birthday']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(num_employees):
            name = fake.name()
            hiring_date = generate_hiring_date()
            department = generate_department()
            birthday = generate_birthday()

            writer.writerow({'Name': name, 'Hiring Date': hiring_date, 'Department': department, 'Birthday': birthday})

# Generate 1000 employee records
generate_data(1000)

print("Employee data has been generated and saved to database.csv")