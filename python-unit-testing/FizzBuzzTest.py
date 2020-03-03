# Test-Driven Development

# always start a test suite with test_
def fizzBuzz(param):
    if (param % 3) == 0 and (param % 5) == 0:
        return "FizzBuzz"
    elif (param % 3) == 0:
        return "Fizz"
    elif (param % 5) == 0:
        return "Buzz"
    else:
        return str(param)


def checkfizzBuzz(param, expectedvalue):
    retval = fizzBuzz(param)
    assert retval == expectedvalue
# not needed anymore since the below testcase
# confirms that the fizzbuzz() can be called
# def test_canCallFizzBuzz():
#     fizzBuzz(1)
#

def test_get1whenpass1():
    checkfizzBuzz(1, "1")


def test_get2whenpass2():
    checkfizzBuzz(2, "2")


def test_getFizzwhenpass3():
    retval = fizzBuzz(3)
    assert retval == "Fizz"


def test_getBuzzwhenpass5():
    retval = fizzBuzz(5)
    assert retval == "Buzz"


def test_getFizzwhenpass6():
    retval = fizzBuzz(6)
    assert retval == "Fizz"


def test_getBuzzwhenpass10():
    retval = fizzBuzz(10)
    assert retval == "Buzz"


def test_getFizzBuzzwhenpass15():
    retval = fizzBuzz(15)
    assert retval == "FizzBuzz"
