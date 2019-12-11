import random

Feet_in_Mile = 5280
Meters_in_Kilometer = 1000


def Get_File_ext(filename):
    return filename[filename.index('.') + 1:]


def Roll_Dice(num):
    return random.randint(1, num)