class Animal:
    def speak(self):
        print("Animal Speaking")


class Dog(Animal):
    def bark(self):
        print("Dog Barking")


class DogActivity(Dog):
    def eat(self):
        print("Dog is eating")


d = DogActivity()
d.bark()
d.speak()
d.eat()


class Arithmetic:
    def sum(self, a, b):
        return a+b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        return a/b


class Derived(Arithmetic):
    def sum(self, a, b):  # example of method overidding
        return a * b


d = Derived()
print(d.div(1, 2))
print(d.mul(1, 2))
# the sum that is called is of the derived class and
# wont take into consideration the function of base class
print(d.sum(1, 2))
