

# ---- NUMBER INPUT ----
def getNum(prompt, allowZero):
    ok = False
    while not ok:
        s = input(prompt)
        try:
            f = float(s)
            if f < 0:
                print("Error: Value cannot be negative.")
            elif f == 0 and not allowZero:
                print("Error: Value must be greater than zero.")
            else:
                ok = True
                return f
        except:
            print("Error: Enter a number.")

# ---- INPUT ----
fDeposit = getNum("Enter Deposit: ", False)
fRatePercent = getNum("Enter Interest Rate Percentage: ", False)
iMonths = int(getNum("Enter Number of Months: ", False))
fGoal = getNum("Enter Goal Amount: ", True)

# ---- RATE ----
fRate = (fRatePercent / 100.0) / 12.0

# ---- MONTHLY OUTPUT ----
print("\nMONTHLY OUTPUT")
print("------------------")

fBal = fDeposit
i = 1

while i <= iMonths:
    fInt = fBal * fRate
    fBal = fBal + fInt
    print("Month " + str(i) + " Balance: $" + format(fBal, ",.2f"))
    i = i + 1

# ---- GOAL OUTPUT ----
print("\nGOAL OUTPUT")
print("--------------")

fBal2 = fDeposit
i = 0

while fBal2 < fGoal:
    fInt = fBal2 * fRate
    fBal2 = fBal2 + fInt
    i = i + 1

print("Goal Amount: $" + format(fGoal, ",.2f"))
print("Months Needed: " + str(i))
print("Final Balance: $" + format(fBal2, ",.2f"))
