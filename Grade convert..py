# Grade Analyzer Program
# CIT-115/115L Python
# Trevon A.

# 1. Ask for person's name
name = input("Enter the person's name: ")

# 2. Ask for four test scores
test1 = float(input("Enter Test 1 score: "))
test2 = float(input("Enter Test 2 score: "))
test3 = float(input("Enter Test 3 score: "))
test4 = float(input("Enter Test 4 score: "))

# 3. Check for negative scores
if test1 < 0 or test2 < 0 or test3 < 0 or test4 < 0:
    print("Test scores must be greater than 0.")
    quit()

# 4. Ask if lowest grade should be dropped
drop = input("Drop the lowest grade? (Y or N): ")

if drop != "Y" and drop != "N":
    print("Enter Y or N to drop the lowest grade.")
    quit()

# 5. Calculate average
if drop == "Y":
    lowest = min(test1, test2, test3, test4)
    total = test1 + test2 + test3 + test4 - lowest
    average = total / 3
else:
    average = (test1 + test2 + test3 + test4) / 4

# 6. Determine letter grade
if average >= 97.0:
    grade = "A+"
elif average >= 94.0:
    grade = "A"
elif average >= 90.0:
    grade = "A-"
elif average >= 87.0:
    grade = "B+"
elif average >= 84.0:
    grade = "B"
elif average >= 80.0:
    grade = "B-"
elif average >= 77.0:
    grade = "C+"
elif average >= 74.0:
    grade = "C"
elif average >= 70.0:
    grade = "C-"
elif average >= 67.0:
    grade = "D+"
elif average >= 64.0:
    grade = "D"
elif average >= 60.0:
    grade = "D-"
else:
    grade = "F"

# 7. Display results
print("Name:", name)
print("Average:", round(average, 1))
print("Letter Grade:", grade)
