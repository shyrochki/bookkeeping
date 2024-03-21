import sys
import csv

def read_database(filename):
    with open(filename, newline='') as file:
        return [row for row in csv.reader(file)][1:]

def generate_report(records, month):
    birthdays = {}
    anniversaries = {}
    for record in records:
        _, hire_date, department, birth_date = record
        hire_month, birth_month = hire_date.split('-')[1], birth_date.split('-')[1]
        if hire_month.lower() == month.lower():
            anniversaries[department] = anniversaries.get(department, 0) + 1
        if birth_month.lower() == month.lower():
            birthdays[department] = birthdays.get(department, 0) + 1
    return birthdays, anniversaries

def print_report(month, birthdays, anniversaries):
    print(f"Report for {month.capitalize()} generated")
    print("--- Birthdays ---")
    print(f"Total: {sum(birthdays.values())}")
    for dept, count in birthdays.items():
        print(f"- {dept}: {count}")
    print("--- Anniversaries ---")
    print(f"Total: {sum(anniversaries.values())}")
    for dept, count in anniversaries.items():
        print(f"- {dept}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python report.py database.csv month")
        sys.exit(1)
    filename, month = sys.argv[1], sys.argv[2]
    records = read_database(filename)
    birthdays, anniversaries = generate_report(records, month)
    print_report(month, birthdays, anniversaries)
