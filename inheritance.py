class Mammal: #inheritance is a mechanism for reusing codes
    def walk(self):
        print("Wait")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.be_annoying()