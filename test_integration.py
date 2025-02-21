import pytest
from product_module import add_product
from order_module import calculate_total_price

@pytest.fixture
def setup_products():
    add_product(1, "Laptop", 1200)
    add_product(2, "Mouse", 20)

# Тест без отстъпка
def test_order_without_discount(setup_products):
    order_items = [(2, 3)]  # 3x Mouse (20 * 3 = 60)
    total_price = calculate_total_price(order_items)
    assert total_price == 60

# Тест с 5% отстъпка
def test_order_with_5_percent_discount(setup_products):
    order_items = [(2, 30)]  # 30x Mouse (20 * 30 = 600) → 5% отстъпка (570)
    total_price = calculate_total_price(order_items)
    assert total_price == 570

# Тест с 10% отстъпка
def test_order_with_10_percent_discount(setup_products):
    order_items = [(1, 1), (2, 5)]  # 1x Laptop (1200) + 5x Mouse (20 * 5 = 100) = 1300
    total_price = calculate_total_price(order_items)
    assert total_price == 1170  # 10% отстъпка
