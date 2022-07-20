from plotholder.src.data_producer import random_float_series, random_integer_series

def test_integer_data_series_no_limits():
    random_ints = random_integer_series(100)
    assert len(random_ints) == 100
    for i in random_ints:
        assert type(i) == int
        assert 0 <= i <= 10000

def test_integer_data_series_limits():
    random_ints = random_integer_series(200,-50,50)
    assert len(random_ints) == 200
    for i in random_ints:
        assert type(i) == int
        assert -50 <= i <= 50

def test_float_data_series_no_limits():
    random_floats = random_float_series(100)
    assert len(random_floats) == 100
    for i in random_floats:
        assert type(i) == float
        assert 0 <= i <= 10000

def test_float_data_series_limits():
    random_floats = random_float_series(200,-250,-50)
    assert len(random_floats) == 200
    for i in random_floats:
        assert type(i) == float
        assert -250 <= i <= -50
