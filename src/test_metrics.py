from metrics import (
    load_data,
    get_total_revenue,
    get_total_profit,
    get_total_quantity,
    get_region_performance,
    get_category_performance,
    get_channel_performance,
    get_profit_margin,
    get_average_order_revenue,
    get_monthly_performance,
    get_top_products,
)


def test_load_data():
    df = load_data()
    assert not df.empty


def test_total_revenue():
    df = load_data()
    assert get_total_revenue(df) > 0


def test_total_profit():
    df = load_data()
    assert get_total_profit(df) > 0


def test_total_quantity():
    df = load_data()
    assert get_total_quantity(df) > 0


def test_region_performance():
    df = load_data()
    result = get_region_performance(df)
    assert not result.empty


def test_category_performance():
    df = load_data()
    result = get_category_performance(df)
    assert not result.empty


def test_channel_performance():
    df = load_data()
    result = get_channel_performance(df)
    assert not result.empty


def test_profit_margin():
    df = load_data()
    result = get_profit_margin(df)
    assert result >= 0


def test_average_order_revenue():
    df = load_data()
    result = get_average_order_revenue(df)
    assert result > 0


def test_monthly_performance():
    df = load_data()
    result = get_monthly_performance(df)
    assert not result.empty


def test_top_products():
    df = load_data()
    result = get_top_products(df)
    assert not result.empty