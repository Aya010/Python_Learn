"""
There is a class about person's infomation.
"""
class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        if gender == 0:
            self.gender = "Male"
        else:
            self.gender = "Female"
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def __str__(self):
        return "Name:%s\nAge:%d\nGender:%s" % (self.name, self.age, self.gender)
