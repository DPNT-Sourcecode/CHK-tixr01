from lib.solutions.checkout import checkout
import pytest


@pytest.parametrize('test_string, expected_price', [
	('2A 2B 3C', 205)
])
def test_checkout(test_string, expected_price):
	assert checkout(test_string) == expected_price
