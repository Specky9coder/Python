class Student:
    def __init__(self, name, major,gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


class Students_female:
    def __init__(self,name, major, gpa, is_intern_or_not):
        self.name = name
        self.major = name
        self.gpa = gpa
        self.is_intern_or_not = is_intern_or_not


class Students_Mobile:
    def __init__(self, Model, Operating_system, A_version, is_Costly_or_not):
        self.Model = Model
        self.Operating_system = Operating_system
        self.A_version = A_version
        self.is_Costly_or_not = is_Costly_or_not


class Students_female_Mobile:
    def __init__(self, Model, Operating_system, A_version, is_Costley_or_not):
        self.Model = Model
        self.Operating_system = Operating_system
        self.A_version = A_version
        self.is_Costly_or_not = is_Costley_or_not


class Students_with_Laptops:
    def __init__(self, L_type, Operating_system, Price, ):
        self.L_type = L_type
        self.Operating_system = Operating_system
        self.Price = Price



class intelligent_Student:
    def __init__(self, intelligent, A_student, Ab_a_student, is_intelligent_or_not):
        self.intelligent = intelligent
        self.A_student = A_student
        self.Ab_a_student = Ab_a_student
        self.is_intelligent_or_not = is_intelligent_or_not

class Students_with_male_or_female():
    def __init__(self, Male_ratio, Female_ratio, Ratio_by_category):
        self.Male_ratio = Male_ratio
        self.Female_ratio = Female_ratio
        self.Ratio_by_category = Ratio_by_category

    def Male_ratio(self):
        if self.Male_ratio >= 55:
            return True

        else:
            print('Male Ratio Is Lower Than The Female Ratio')

            return


    def Female_ratio(self):
        if self.Female_ratio <= 45:
            print('Female Ratio Is 45 Or 45 Lower Than The Male Ratio')
            return

        else:
            return False

