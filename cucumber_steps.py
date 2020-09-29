import sys

from pytest_bdd import scenario, parsers, given, when, then

sys.path.append("C://Users//tibi//Documents//tau-pytest-bdd//tests//cucumbers.py")
from cucumbers import CucumberBasket

@scenario("../feature/cucumbers.feature","Add cucumbers to a basket")
EXTRA_TYPES = {
    'Number' : int,
}
def test_add():
    pass


@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=dict(EXTRA_TYPES)))
def basket(initial):
    return CucumberBasket(initial_count=initial)

@when(parsers.cfparse('they are added "{some:Number}" cucumbers to the basket', extra_types=dict(EXTRA_TYPES)))
def add_cucumbers(basket, some):
    basket.add(some)

@then(parsers.cfparse('the basket has "{total:Number}" cucumbers', extra_types=dict(EXTRA_TYPES)))
def basket_has_total(basket, total):
    assert basket = total


@scenario("../feature/cucumbers.feature" , "Remove cucumbers from a basket")
def test_remove():
    pass

@given(parsers.cfparse('The basket has "{initial:Number}" cucumbers', extra_types=dict(EXTRA_TYPES)))
def basket(initial):
    return CucumberBasket(initial_count=initial)

@when(parsers.cfparse('They are removed "{some:Number}" from the basket', extra_types=dict(EXTRA_TYPES)))
def remove_cucumbers(basket, some):
    basket.remove(some)

@then(parsers.cfparse('The basket has "{total:Number}" cucumbers.', extra_types=dict(EXTRA_TYPES)))
def total(basket, total):
    assert basket = total