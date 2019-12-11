class Student():
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    def is_in_criteria(self):
        if self.gpa > 3.5:
            return ('Congratulatons You Are Eligible For The Company')
        else:
            print('Sorry You Are Not Eligible For This Company')
            return('')



    def Students(self, Male_ratio, Female_ratio, ratio_by_category):
        self.Male_ratio = Male_ratio
        self.Female_ratio = Female_ratio
        self.ratio_by_category = ratio_by_category









