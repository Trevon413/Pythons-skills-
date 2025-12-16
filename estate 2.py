def getFloatInput(prompt):
    while True:
        value = input(prompt)

        if value.replace(".", "", 1).isdigit() == False:
            print("Invalid input.")
        elif float(value) <= 0:
            print("Value must be greater than zero.")
        else:
            return float(value)


def getMedian(numbers):
    numbers.sort()
    count = len(numbers)

    if count % 2 == 1:
        return numbers[count // 2]
    else:
        return (numbers[count // 2 - 1] + numbers[count // 2]) / 2


def main():
    sales = []
    choice = "Y"

    while choice == "Y":
        price = getFloatInput("Enter property sales price: ")
        sales.append(price)

        choice = input("Enter another value Y or N: ")
        while choice != "Y" and choice != "N":
            choice = input("Enter another value Y or N: ")

    sales.sort()

    total = 0
    for value in sales:
        print("$" + format(value, ".2f"))
        total = total + value

    print("Minimum: $" + format(min(sales), ".2f"))
    print("Maximum: $" + format(max(sales), ".2f"))
    print("Total: $" + format(total, ".2f"))
    print("Average: $" + format(total / len(sales), ".2f"))
    print("Median: $" + format(getMedian(sales), ".2f"))
    print("Commission: $" + format(total * 0.03, ".2f"))


main()
