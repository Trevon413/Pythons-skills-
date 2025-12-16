# Compound Interest Calculator

# Ask the user for the principal amount (PV)
principal = float(input("Enter the principal amount: "))

# Ask the user for the annual interest rate in percent (R)
interest_rate_percent = float(input("Enter the annual interest rate (in %): "))

# Ask the user for the number of years (t)
years = float(input("Enter the number of years: "))

# Ask the user for the number of times the interest is compounded per year (m)
compounds_per_year = int(input("Enter the number of compounding periods per year: "))

# Convert the interest rate from percent to a decimal
rate = interest_rate_percent / 100

# Calculate the future value (FV) using the compound interest formula
future_value = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)

# Print the result formatted as a currency value with two decimal places
print(f"The future value is: ${future_value:,.2f}")
