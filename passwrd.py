
# Trevon Alexander
# Password Validator
# Reflection Questions
# I like that this assignment kind of made you go back into what you've learned and to apply it with 
# Hard part about this assignment was using the only things from the list without any other styles. Struggled with the passowrd part for a few
# Not sure if its efficent, i think i might have worked to hard and did extra coding
# 1.Lerarned coding is hard and difficult
# 2. Self reflection, i am no where near where i should. need to implement more time in learning



def GetInitialsTA(sNameTA):
    sNameTA = sNameTA.strip()

    iSpaceTA = sNameTA.find(" ")
    if iSpaceTA == -1:
        sFirstTA = sNameTA
        sLastTA = ""
    else:
        sFirstTA = sNameTA[:iSpaceTA].strip()
        sLastTA = sNameTA[iSpaceTA + 1:].strip()

    sInitialsTA = ""
    if len(sFirstTA) > 0:
        sInitialsTA = sInitialsTA + sFirstTA[0]
    if len(sLastTA) > 0:
        sInitialsTA = sInitialsTA + sLastTA[0]

    return sInitialsTA


def HasUpperTA(sTextTA):
    bHasUpperTA = False
    for sChTA in sTextTA:
        if sChTA.isupper():
            bHasUpperTA = True
    return bHasUpperTA


def HasLowerTA(sTextTA):
    bHasLowerTA = False
    for sChTA in sTextTA:
        if sChTA.islower():
            bHasLowerTA = True
    return bHasLowerTA


def HasDigitTA(sTextTA):
    bHasDigitTA = False
    for sChTA in sTextTA:
        if sChTA.isdigit():
            bHasDigitTA = True
    return bHasDigitTA


def HasSpecialTA(sTextTA):
    sSpecialsTA = "_!@#$%^"
    bHasSpecialTA = False
    for sChTA in sTextTA:
        if sChTA in sSpecialsTA:
            bHasSpecialTA = True
    return bHasSpecialTA


def ContainsInitialsTA(sPasswordTA, sInitialsTA):
    if sInitialsTA == "":
        return False
    return (sInitialsTA.lower() in sPasswordTA.lower())


def CheckDuplicatesTA(sPasswordTA):
    # returns a list like: [["a", 2], ["$", 3]] (case-insensitive)
    lCharsTA = []
    lCountsTA = []
    lDupTA = []

    for sChTA in sPasswordTA:
        sKeyTA = sChTA.lower()

        iIndexTA = -1
        iTA = 0
        while iTA < len(lCharsTA):
            if lCharsTA[iTA] == sKeyTA:
                iIndexTA = iTA
            iTA = iTA + 1

        if iIndexTA == -1:
            lCharsTA.append(sKeyTA)
            lCountsTA.append(1)
        else:
            lCountsTA[iIndexTA] = lCountsTA[iIndexTA] + 1

    iTA = 0
    while iTA < len(lCharsTA):
        if lCountsTA[iTA] > 1:
            lDupTA.append([lCharsTA[iTA], lCountsTA[iTA]])
        iTA = iTA + 1

    return lDupTA


def main():
    sNameTA = input("Enter your first and last name: ")
    sInitialsTA = GetInitialsTA(sNameTA)

    while True:
        sPasswordTA = input("Enter your desired password: ").strip()
        bValidTA = True

        # 6) length 8 to 12
        if len(sPasswordTA) < 8 or len(sPasswordTA) > 12:
            print("Password must be between 8 and 12 characters.")
            bValidTA = False

        # 7) can't start with Pass or pass
        if sPasswordTA.lower().startswith("pass"):
            print("Password can't start with Pass.")
            bValidTA = False

        # 8) at least 1 uppercase
        if HasUpperTA(sPasswordTA) == False:
            print("Password must contain at least 1 uppercase letter.")
            bValidTA = False

        # 9) at least 1 lowercase
        if HasLowerTA(sPasswordTA) == False:
            print("Password must contain at least 1 lowercase letter.")
            bValidTA = False

        # 10) at least 1 number
        if HasDigitTA(sPasswordTA) == False:
            print("Password must contain at least 1 number.")
            bValidTA = False

        # 11) at least 1 special: _ ! @ # $ % ^
        if HasSpecialTA(sPasswordTA) == False:
            print("Password must contain at least 1 of these special characters: _ ! @ # $ % ^")
            bValidTA = False

        # 12) must not contain initials (any case)
        if ContainsInitialsTA(sPasswordTA, sInitialsTA):
            print("Password must not contain user initials.")
            bValidTA = False

        # 13) no character (case-insensitive) can appear more than once
        lDupTA = CheckDuplicatesTA(sPasswordTA)
        if len(lDupTA) > 0:
            print("These characters appear more than once:")
            iTA = 0
            while iTA < len(lDupTA):
                print(lDupTA[iTA][0] + " appears " + str(lDupTA[iTA][1]) + " times")
                iTA = iTA + 1
            bValidTA = False

        # 14) if valid
        if bValidTA:
            print("Password is valid and OK to use.")
            break
        


main()
