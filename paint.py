import math

def getFloatInput(promptS):
    valid = False
    while valid == False:
        valueS = input(promptS)
        try:
            valueF = float(valueS)
            if valueF > 0:
                valid = True
            else:
                print("Enter a number greater than zero.")
        except:
            print("Enter a valid number.")
    return valueF

def getGallonsOfPaint(squareFeetF, feetPerGallonF):
    gallonsF = squareFeetF / feetPerGallonF
    gallonsF = math.ceil(gallonsF)
    return float(gallonsF)

def getLaborHours(squareFeetF, laborHoursPerGallonF):
    hoursF = squareFeetF / laborHoursPerGallonF
    return float(hoursF)

def getLaborCost(laborHoursF, laborChargePerHourF):
    return laborHoursF * laborChargePerHourF

def getPaintCost(gallonsF, paintPriceF):
    return gallonsF * paintPriceF

def getSalesTax(stateS):
    stateS = stateS.upper()
    if stateS == "CT":
        return 0.06
    elif stateS == "MA":
        return 0.0625
    elif stateS == "ME":
        return 0.085
    elif stateS == "NH":
        return 0.00
    elif stateS == "RI":
        return 0.07
    elif stateS == "VT":
        return 0.06
    else:
        return 0.0

def showCostEstimate(gallonsF, laborHoursF, laborCostF, paintCostF, taxRateF, totalCostF):
    print("Gallons Needed: " + str(gallonsF))
    print("Labor Hours: " + str(laborHoursF))
    print("Labor Cost: " + str(laborCostF))
    print("Paint Cost: " + str(paintCostF))
    print("Tax Rate: " + str(taxRateF))
    print("Total Cost: " + str(totalCostF))

squareFeetF = getFloatInput("Enter Square Feet of Wall: ")
paintPriceF = getFloatInput("Enter Paint Price: ")
feetPerGallonF = getFloatInput("Enter Feet per Gallon: ")
laborHoursPerGallonF = getFloatInput("Enter Labor Hours per Gallon: ")
laborChargePerHourF = getFloatInput("Enter Labor Charge per Hour: ")

customerNameS = input("Enter Customer Last Name: ")
stateS = input("Enter State Initials (CT, MA, ME, NH, RI, VT): ")

gallonsF = getGallonsOfPaint(squareFeetF, feetPerGallonF)
laborHoursF = getLaborHours(squareFeetF, laborHoursPerGallonF)
laborCostF = getLaborCost(laborHoursF, laborChargePerHourF)
paintCostF = getPaintCost(gallonsF, paintPriceF)
taxRateF = getSalesTax(stateS)

totalCostF = (laborCostF + paintCostF) * (1 + taxRateF)

showCostEstimate(gallonsF, laborHoursF, laborCostF, paintCostF, taxRateF, totalCostF)
