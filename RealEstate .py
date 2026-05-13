# Name: Trevon Alexander
# Code Name: Real Estate Analyzer

# Reflection:
# This assignment, made me use new skills that I haven't before so I liked that it made me get out my comfort zone.
# For the longest I couldn't get the document to show in my Python file, I thought I was coding it right, but I guess my files had to be in the same location for it to be read.
# One Mistake I did make was I don't know if I understood the instructions correctly. I didn't use all of the data. I didn't know if it was a choice of how much to use so my code my reflect. 











def getDataInput():
    lRecordsBLC = []

    fFileBLC = open("RealEstateData.csv", "r",)

    for sLineBLC in fFileBLC:
        lRecordsBLC.append(sLineBLC.strip())

    fFileBLC.close()

    return lRecordsBLC


# Function to calculate median
def getMedian(lValuesBLC):

    lValuesBLC.sort()

    iCountBLC = len(lValuesBLC)

    if iCountBLC % 2 == 1:
        iMiddleBLC = iCountBLC // 2
        fMedianBLC = lValuesBLC[iMiddleBLC]

    else:
        iMiddleBLC = iCountBLC // 2
        fMedianBLC = (lValuesBLC[iMiddleBLC] + lValuesBLC[iMiddleBLC - 1]) / 2

    return fMedianBLC


def main():

    lRecordsBLC = getDataInput()

    lPricesBLC = []

    dCityTotalsBLC = {}
    dZipTotalsBLC = {}
    dTypeTotalsBLC = {}

    for sRecordBLC in lRecordsBLC[1:]:

        lFieldsBLC = sRecordBLC.split(",")

        sCityBLC = lFieldsBLC[1]
        sZipBLC = lFieldsBLC[2]
        sTypeBLC = lFieldsBLC[7]

        fPriceBLC = float(lFieldsBLC[8])

        lPricesBLC.append(fPriceBLC)

        if sCityBLC in dCityTotalsBLC:
            dCityTotalsBLC[sCityBLC] += fPriceBLC
        else:
            dCityTotalsBLC[sCityBLC] = fPriceBLC

        if sZipBLC in dZipTotalsBLC:
            dZipTotalsBLC[sZipBLC] += fPriceBLC
        else:
            dZipTotalsBLC[sZipBLC] = fPriceBLC

        if sTypeBLC in dTypeTotalsBLC:
            dTypeTotalsBLC[sTypeBLC] += fPriceBLC
        else:
            dTypeTotalsBLC[sTypeBLC] = fPriceBLC


    lPricesBLC.sort()

    fMinBLC = lPricesBLC[0]
    fMaxBLC = lPricesBLC[-1]
    fTotalBLC = sum(lPricesBLC)
    fAvgBLC = fTotalBLC / len(lPricesBLC)
    fMedianBLC = getMedian(lPricesBLC)

    print("Minimum Price: $", format(fMinBLC, ".2f"))
    print("Maximum Price: $", format(fMaxBLC, ".2f"))
    print("Total Price: $", format(fTotalBLC, ".2f"))
    print("Average Price: $", format(fAvgBLC, ".2f"))
    print("Median Price: $", format(fMedianBLC, ".2f"))

    print("\nCity Totals")
    for sCityBLC in dCityTotalsBLC:
        print(sCityBLC, "$", format(dCityTotalsBLC[sCityBLC], ".2f"))

    print("\nZip Totals")
    for sZipBLC in dZipTotalsBLC:
        print(sZipBLC, "$", format(dZipTotalsBLC[sZipBLC], ".2f"))

    print("\nProperty Type Totals")
    for sTypeBLC in dTypeTotalsBLC:
        print(sTypeBLC, "$", format(dTypeTotalsBLC[sTypeBLC], ".2f"))


main()
