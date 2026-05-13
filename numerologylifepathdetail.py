# Name: YourName
# Assignment: NumerologyLifePathDetails


from numerology import Numerology


class Numerologylifepathdetail(Numerology):
    def __init__(self, name, birthdate):
        clean_bday = birthdate.replace("-", "").replace("/", "")

        if not name.strip():
            raise ValueError("Name cannot be empty.")

        if len(clean_bday) != 8 or not clean_bday.isdigit():
            raise ValueError("Birthdate must be in mm-dd-yyyy or mm/dd/yyyy format.")

        super().__init__(clean_bday, name)

    @property
    def Name(self):
        return self.name

    @property
    def Birthdate(self):
        return self.bday

    @property
    def BirthDay(self):
        return self.get_birthday_num()

    @property
    def LifePath(self):
        return self.get_life_path_num()

    @property
    def Attitude(self):
        return self.get_attitude_num()

    @property
    def Soul(self):
        return self.get_soul_num()

    @property
    def Personality(self):
        return self.get_personality_num()

    @property
    def PowerName(self):
        return self.get_power_name_num()

    @property
    def LifePathDescription(self):
        descriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often an extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }
        return descriptions[self.LifePath]

