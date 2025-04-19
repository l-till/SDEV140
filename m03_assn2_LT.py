# m03_assn2_LT.py
# Logan Till
# 2025-04-06
# Read Contractors File
# Coding assistance was used in this program


# this will print the title of the program
print("***************************************")
print("Read Contractors File (by Logan Till)")
print("***************************************\n")

# this will print the welcome message
print("Welcome!")
print("This program will read data from a contractors file.\n")

# Import Libraries

# Output File
FILE_NAME = "contractors.txt"

# Constants
HOURS_PER_YEAR = 2080

# Variables
contractors = []
operations_contractors = []
total_hourly = 0
total_earnings = 0
total_ops_earnings = 0
contractor_count = 0
ops_count = 0
highest_earner = None
lowest_earner = None

# Read the file and store the data in a list
with open(FILE_NAME, 'r') as file:
    for line in file:
        fields = line.strip().split('|')

        # Validates if the contractor is active and skips if not
        if fields[6].lower() != 'active':
            continue

        # Extract fields
        department = fields[0]
        hourly_rate = float(fields[2])
        lname = fields[3]
        fname = fields[4][0]

        # Calculations
        earnings = hourly_rate * HOURS_PER_YEAR
        total_hourly += hourly_rate
        total_earnings += earnings
        contractor_count += 1

        # Create contractors record
        contractor = {
        "name": f"{lname}, {fname}",
        'department': department,
        'hourly_rate': hourly_rate,
        'earnings': earnings
        }
        contractors.append(contractor)

        # CodingAssistAI: This code was added by built in Copilot AI
        # Track Operations department
        if department.lower() == "operations":
            operations_contractors.append(contractor)
            total_ops_earnings += earnings
            ops_count += 1
        # Track highest and lowest earners
        if highest_earner is None or earnings > highest_earner['earnings']:
            highest_earner = contractor

        if lowest_earner is None or earnings < lowest_earner['earnings']:
            lowest_earner = contractor


# Display results
# Header
print(f"{'Contractor':<20} {'Department':<15} {'Hourly Rate':>12} {'Annual Earnings':>16}")
# Contractors
for contractor in contractors:
    print(f"{contractor['name']:<20} {contractor['department']:<15} {contractor['hourly_rate']:>12,.2f} {contractor['earnings']:>16,.2f}")

# Contractor summary
print("# of active contractors:", contractor_count)
print("Total hourly rate:", total_hourly)
print("Total Earnings: ", total_earnings, "\n")

# Earnings summary
print(f"Highest Earner: {highest_earner['name']}{highest_earner['earnings']:.2f}")
print(f"Lowest Earner: {lowest_earner['name']}{lowest_earner['earnings']:.2f}")

# Operations summary
print(f"\n# of Operations contractors {ops_count}")
print(f"Operations total earnings: {total_ops_earnings:.2f}")

# This will print the goodbye message
print("\nThank you for using this program.")