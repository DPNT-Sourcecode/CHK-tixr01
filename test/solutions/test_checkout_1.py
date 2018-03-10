from lib.solutions.checkout import checkout
import pytest


@pytest.mark.parametrize('test_string, expected_price', [
	('EE', 80),
	('EEEEBB', 160),
	('BEBEEE', 160),
	('EE', 80)
])
def test_checkout(test_string, expected_price):
	assert checkout(test_string) == expected_price
