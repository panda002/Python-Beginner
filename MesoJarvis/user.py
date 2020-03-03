from MesoJarvis.library1 import Base
from MesoJarvis.test_cal import isPrime

# first we need to check if the function
# is actually present in the base class
# before we can implement the same in our
# derived class

assert hasattr(Base, 'foo')


class Derived(Base):
    def bar(self):
        return 'bar'


a = int(input("Enter a number: "))


class Drived2(isPrime(a)):
    def isPrime(self):
        self.isPrime()


