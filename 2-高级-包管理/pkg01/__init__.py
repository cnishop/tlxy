
def inInit():
    print("I am in init of package")

class Person():
    def __init__(self, name="NoName", age=18):
        self.name = name
        self.age = age

    def teach(self):
        print("My name is {0}".format(self.name))