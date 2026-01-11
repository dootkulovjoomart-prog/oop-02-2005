class Student:
    def __init__(self , name , age , course):
        self.name = name
        self.age = age
        self.course = course

    def info(self):
        return F'Student: {self.name} , age:{self.age} , course:{self.course}'

    def study(self):
        return f'{self.name}  study in {self.course} course.'


s = Student('Zhoomart', 21, 4)
print(s.info())
print(s.study())


class BankAccount:
    def __init__(self ,owner , balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
       if amount > self.balance:
            return 'Insufficient funds'
            self.balance -= amount
            return self.balance
            def get_balance(self):
                return self.balance

account = BankAccount('Zhoomart', 30000)
print(account.deposit(3456))
print(account.withdraw(40000))

