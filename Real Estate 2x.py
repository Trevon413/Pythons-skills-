


def getDataInput():
    LRecordsTMA = []

    fFileTMA = open("RealEstateData.csv", "r")

    for sLineTMA in fFileTMA:
        LRecordsTMA.append(sLineTMA.strip())

    fFileTMA.close()

    return LRecordsTMA


# Function to calculate median
def getMedian(lValuesTMA):
    lValuesTMA.sort()

    iCountTMA = len(lValuesTMA)

    if iCountTMA % 2 == 1:
        iMiddleTMA = iCountTMA // 2
        fMedianTMA = lValuesTMA[iMiddleTMA]
    else:
        iMiddleTMA = iCountTMA // 2
        fMedianTMA = (lValuesTMA[iMiddleTMA] + lValuesTMA[iMiddleTMA - 1]) / 2

    return fMedianTMA


def main():
    LRecordsTMA = getDataInput()

    LPricesTMA = []

    dCityTotalsTMA = {}
    dZipTotalsTMA = {}
    dTypeTotalsTMA = {}


firstline=True

for sRecordTMA in LRecordsTMA[1:]:
        if firstline:
            Firstline= False
            continue

        lFieldsTMA= sRecordsTMA.split(",")

        sCityTMA = lFieldsTMA[1]
        sZipTMA = lFieldsTMA[2]
        sTypeTMA = lFieldsTMA[7]

        fPriceTMA = float(lFieldsTMA[8])

        lPricesTMA.append(fPriceTMA)

        if sCityTMA in dCityTotalsTMA:
            dCityTotalsTMA[sCityTMA] += fPriceTMA
        else:
            dCityTotalsTMA[sCityTMA] = fPriceTMA

        if sZipTMA in dZipTotalsTMA:
            dZipTotalsTMA[sZipTMA] += fPriceTMA
        else:
            dZipTotalsTMA[sZipTMA] = fPriceTMA

        if sTypeTMA in dTypeTotalsTMA:
            dTypeTotalsTMA[sTypeTMA] += fPriceTMA
        else:
            dTypeTotalsTMA[sTypeTMA] = fPriceTMA

lPricesTMA.sort()

fMinTMA = lPricesTMA[0]
fMaxTMA = lPricesTMA[-1]
fTotalTMA = sum(lPricesTMA)
fAvgTMA = fTotalTMA / len(lPricesTMA)
fMedianTMA = getMedian(lPricesTMA)

print("Minimum Price:", format(fMinTMA, ".2f"))
print("Maximum Price:", format(fMaxTMA, ".2f"))
print("Total Price:", format(fTotalTMA, ".2f"))
print("Average Price:", format(fAvgTMA, ".2f"))
print("Median Price:", format(fMedianTMA, ".2f"))
    
print("\nCity Totals")
for sCityTMA in dCityTotalsTMA.items():
    print(sCityTMA, "$", format(dCityTotalsTMA[sCityTMA], ".2f"))

print(f"{sCityTMA:25s} ${fCityTotals:12,.2f}")
    # Springfield---------  ----, 13,500.00

print("\nZip Totals")
for sZipTMA in dZipTotalsTMA:
        print(sZipTMA, "$", format(dZipTotalsTMA[sZipTMA], ".2f"))

print("\nProperty Type Totals")
for sTypeTMA in dTypeTotalsTMA:
    print(sTypeTMA, "$", format(dTypeTotalsTMA[sTypeTMA], ".2f"))


main()
