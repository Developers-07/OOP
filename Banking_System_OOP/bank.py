# child class : Bank

from user_implement import UserImplement

class Bank(UserImplement):

    def __init__(self, name, age, gender):
        super(Bank, self).__init__(name=name, age=age, gender=gender)

        self.__balance = 0


    def deposit(self, damount):

        self.__damount = damount
        self.__balance = self.__balance + self.__damount
        return self.__balance

    def withdraw(self, wamount):

        self.__wamount = wamount
        if self.__balance > self.__wamount:
            self.__balance = self.__balance - self.__wamount
            return self.__balance
        else:
            return "Balance Insufficient"

u1 = Bank("Zishan", 22, "Male")

u1.show_details()

print("After Deposit total tk = ",u1.deposit(500))
print("After Withdraw total tk = ",u1.withdraw(200))

print("After Deposit total tk = ",u1.deposit(1000))
print("After Withdraw total tk = ",u1.withdraw(500))

