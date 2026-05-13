





class Numerology:
    def __init__(self, bday, name):
        self.bday = bday
        self.name = name

    def reduce_num(self, number):
        while number > 9:
            total = 0
            for digit in str(number):
                total = total + int(digit)
            number = total
        return number

    def get_birthday_num(self):
        bday = self.bday[2:4]
        return self.reduce_num(int(bday))

    def get_life_path_num(self):
        total = 0
        for digit in self.bday:
            total = total + int(digit)
        return self.reduce_num(total)

    def get_attitude_num(self):
        month = int(self.bday [0:2])
        day = int(self.bday [2:4])
        total = month + day
        return self.reduce_num(total)

    def letter_to_num(self, ch):
        return ord(ch.upper()) - 64

    def get_soul_num(self):
        total = 0
        for ch in self.name:
            if ch.upper() in "AEIOU":
                total = total + self.letter_to_num(ch)
        return self.reduce_num(total)

    def get_personality_num(self):
        total = 0
        for ch in self.name:
            if ch.isalpha() and ch.upper() not in "AEIOU":
                total = total + self.letter_to_num (ch)
        return self.reduce_num(total)

    def get_power_name_num(self):
        total = 0
        for ch in self.name:
            if ch.isalpha():
                total = total + self.letter_to_num(ch)
        return self.reduce_num(total)
    
def main():
    name= input("Enter name:")
    bday= input("Enter your birthday (mm-dd-yyyy or mm/dd/yyyy): ")

    bday= bday.replace("/", "")
    bday= bday.replace("-", "")

    person= Numerology(bday, name)


    print(person.name)
    print("Birthday Number:", person.get_birthday_num())
    print("Life Path Number:", person.get_life_path_num())
    print("Attitude Number:", person.get_attitude_num())
    print("Soul Number:", person.get_soul_num())
    print("Personality Number:" , person.get_personality_num())
    print("Power Name:" ,person.get_power_name_num())

if __name__ == "__main__":
    main()
