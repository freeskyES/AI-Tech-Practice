# Inheritance (상속)

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_me(self):
        print("my name is ", self.name, "my age is ", self.age)

    def __str__(self):
        return "my name is ", self.name, "my age is ", self.age

class Korean(Person):
    pass


class Employee(Person):
    def __init__(self, name, age, salary, hire_date):
        super().__init__(name, age)
        self.salary = salary
        self.hire_date = hire_date

    def about_me(self): # 부모 클래스 함수 재정의
        super().about_me() #  부모 클래스 함수 사용
        print("my salary is ", self.salary)



