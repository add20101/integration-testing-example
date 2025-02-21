def apply_discount(total_price):
    """
    Прилага отстъпка към общата цена.
    - 10% отстъпка за поръчки над 1000.
    - 5% отстъпка за поръчки между 500 и 1000 (включително).
    - Няма отстъпка за поръчки до 500.
    """
    if total_price > 1000:
        return total_price * 0.9  # 10% отстъпка
    elif total_price > 500:
        return total_price * 0.95  # 5% отстъпка
    return total_price  # Без отстъпка
