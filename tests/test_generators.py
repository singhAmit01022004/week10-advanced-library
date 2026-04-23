from my_advanced_lib.core.generators import process_data


def test_generator():
    result = list(process_data([1, 2, 3]))
    assert result == [2, 4, 6]