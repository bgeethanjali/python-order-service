from order_service.pricing import apply_discount, format_line, sku_list


def test_apply_discount_none():
    assert apply_discount(100.0) == 100.0


def test_apply_discount_percent():
    assert apply_discount(100.0, 10) == 90.0


def test_format_line():
    assert format_line("A-100", 2, 19.99) == "A-100 x2 @ 19.99"


def test_sku_list():
    items = [{"sku": "A-100"}, {"sku": "B-250"}]
    assert sku_list(items) == ["A-100", "B-250"]
