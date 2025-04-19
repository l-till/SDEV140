# m03_assn2_LT.py
# Logan Till
# 2025-04-06
# Read Contractors File
# Coding assistance was used in this program

# Print program header
print("***************************************")
print("Read Contractors File (by Logan Till)")
print("***************************************\n")

print("Welcome!")
print("This program will read data from a contractors file.\n")

# Configuration
FILE_NAME = "contractors.txt"
HOURS_PER_YEAR = 2080

# Initialize variables
contractors = []
operations_contractors = []
total_hourly = 0.0
total_earnings = 0.0
total_ops_earnings = 0.0
contractor_count = 0
ops_count = 0
highest_earner = None
lowest_earner = None

# Read and process the file

with open(FILE_NAME, 'r') as file:
   for line in file:
      fields = line.strip().split('|')
      
      # Validates if 
      if len(fields) < 7 or fields[6].lower() != 'active':
            continue
            
      # Extract fields
      department = fields[0]
      hourly_rate = float(fields[2])
      last_name = fields[3]
      first_initial = fields[4][0]
      
      # Calculate earnings
      annual_earnings = hourly_rate * HOURS_PER_YEAR
      
      # Create contractor record
      contractor = {
            'name': f"{last_name}, {first_initial}.",
            'department': department,
            'hourly_rate': hourly_rate,
            'annual_earnings': annual_earnings
      }
      contractors.append(contractor)
      
      # Update totals
      total_hourly += hourly_rate
      total_earnings += annual_earnings
      contractor_count += 1
      
      # Track Operations department
      if department.lower() == 'operations':
            operations_contractors.append(contractor)
            total_ops_earnings += annual_earnings
            ops_count += 1
      
      # Track highest and lowest earners
      if highest_earner is None or annual_earnings > highest_earner['annual_earnings']:
            highest_earner = contractor
      if lowest_earner is None or annual_earnings < lowest_earner['annual_earnings']:
            lowest_earner = contractor

# Display results
print(f"{'Contractor':<20} {'Department':<15} {'Hourly Rate':>12} {'Annual Earnings':>16}")
print("-" * 65)

for contractor in contractors:
    print(f"{contractor['name']:<20} {contractor['department']:<15} "
          f"{contractor['hourly_rate']:>12.2f} {contractor['annual_earnings']:>16,.2f}")

print("\nSUMMARY INFORMATION")
print("-" * 65)
print(f"Number of active contractors: {contractor_count}")
print(f"Total hourly rate for all active contractors: {total_hourly:,.2f}")
print(f"Total estimated annual earnings: {total_earnings:,.2f}")
print(f"Highest earner: {highest_earner['name']} (${highest_earner['annual_earnings']:,.2f})")
print(f"Lowest earner: {lowest_earner['name']} (${lowest_earner['annual_earnings']:,.2f})")

print("\nOPERATIONS DEPARTMENT")
print("-" * 65)
print(f"Number of contractors: {ops_count}")
print(f"Total estimated annual earnings: {total_ops_earnings:,.2f}")

# Goodbye message
print("\nThank you for using this program.")