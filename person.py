"""
There is a class about person's infomation.
"""
class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def __str__(self):
        return "Name:%s\nAge:%s\nGender:%s" % (self.name, self.age, self.gender)
