# This is a sample Python script.
from Inheritance import Korean, Person, Employee
from Polymorphism import Cat, Dog


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def inheritance():
    first_korean = Korean("eunsong", 30)
    print(first_korean.name)

    myPerson = Person("eunsong", 30)
    myEmployee = Employee("es", 30, 1000, "2017.03")
    myEmployee.about_me()

def polymorphism():
    animals = [Cat('missy'),
               Cat('Mr. Mistoffelees'),
               Dog('Lassie')]
    for animal in animals:
        print(animal.name + ': '+ animal.talk())


if __name__ == '__main__':
    print_hi('PyCharm')
    inheritance()
    polymorphism()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
