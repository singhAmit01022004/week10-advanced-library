from my_advanced_lib.core.decorators import retry


def test_retry_success():
    @retry(3)
    def func():
        return 10

    assert func() == 10