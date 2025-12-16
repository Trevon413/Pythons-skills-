print("Trevon A Temp Converter")

t = float(input("Enter a temperature: "))
s = input("Is the temp F for Fahrenheit or C for Celsius? ")

if s == "F" or s == "f":
    if t > 212:
        print("Temp can not be > 212")
    else:
        print("The Celsius equivalent is:", round((t - 32) * 5.0 / 9, 1))

elif s == "C" or s == "c":
    if t > 100:
        print("Temp can not be > 100")
    else:
        print("The Fahrenheit equivalent is:", round(t * 9.0 / 5 + 32, 1))

else:
    print("Enter a F or C")
