from numerologylifepathdetail import Numerologylifepathdetail


def main():
    name = input("Enter name: ")
    bday = input("Enter your birthday (mm-dd-yyyy or mm/dd/yyyy): ")

    person = Numerologylifepathdetail(name, bday)

    print("Name:", person.Name)
    print("Birthdate:", person.Birthdate)
    print("Birthday Number:", person.BirthDay)
    print("Life Path Number:", person.LifePath)
    print("Attitude Number:", person.Attitude)
    print("Soul Number:", person.Soul)
    print("Personality Number:", person.Personality)
    print("Power Name Number:", person.PowerName)
    print("Life Path Description:", person.LifePathDescription)


if __name__ == "__main__":
    main()
