
from user import User

class UserImplement(User):

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def show_details(self):
        print("Name = "+self.__name + " Age =",self.__age," Gender = "+self.__gender)

#u1 = UserImplement("Zishan", 22, "Male")

#u1.show_details()