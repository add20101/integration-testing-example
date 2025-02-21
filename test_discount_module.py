import pytest
from discount_module import apply_discount

def test_no_discount():
    assert apply_discount(500) == 500  # Без отстъпка

def test_5_percent_discount():
    assert apply_discount(600) == 570  # 5% отстъпка

def test_10_percent_discount():
    assert apply_discount(1100) == 990  # 10% отстъпка
