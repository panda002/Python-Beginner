from .checkout import Checkout
import pytest


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_price("a", 1)
    checkout.add_item_price("b", 1)
    return checkout


# def test_canadditemprice(checkout):
#     checkout.addItemPrice("a", 1)
#
#
# def test_canadditem(checkout):
#     checkout.addItem("a")
#

def test_can_calculate_total(checkout):
    checkout.add_item("a")
    assert checkout.calculate_total() == 1


def test_get_correct_total_for_multiple_items(checkout):
    checkout.add_item("a")
    checkout.add_item("b")
    assert checkout.calculate_total() == 2


def test_can_add_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)


def test_can_apply_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)
    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("a")
    assert checkout.calculate_total() == 2


def test_exception_with_bad_item(checkout):
    with pytest.raises(Exception):
        checkout.add_item("c")
