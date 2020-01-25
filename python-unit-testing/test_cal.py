import pytest

import cal


@pytest.mark.parametrize('num1, num2, result',
                         [
                             (10, 5, 15),
                             ("hello", "tony", "hellotony")]

                         )
def test_add(num1, num2, result):
    assert cal.add(num1, num2) == result


# def test_add_string():
# assert cal.add("hello", "tony") == "hellotony"


def test_sub():
    assert cal.sub(10, 5) == 5
