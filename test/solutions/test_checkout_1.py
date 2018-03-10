from lib.solutions.checkout import checkout
import pytest


@pytest.mark.parametrize('test_string, expected_price', [
	('AABBCCC', 205)
])
def test_checkout(test_string, expected_price):
	assert checkout(test_string) == expected_price
