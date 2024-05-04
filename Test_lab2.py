import lab2

def test_find_min_max():
    result = []
    input = [33, 57, 73, 24, 61, 49]
    minMax = [24, 73]

    result = lab2.calc_min_max_temperature(input)

    assert (result == minMax)


def test_calc_average():
    result = 0
    input = [33, 57, 73, 24, 61, 49]
    average = 49.5

    result = lab2.calc_average_temperature(input)

    assert (result == average)


def test_calc_median_temperature():
    result = 0
    list = [24, 33, 49, 57, 61, 73]
    median = 53.0
    
    result = lab2.calc_median_temperature(list)

    assert (result == median)