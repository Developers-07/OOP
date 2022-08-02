
from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def set_age(self, age):
        pass

    @abstractmethod
    def get_gender(self):
        pass

    @abstractmethod
    def set_gender(self, gender):
        pass
