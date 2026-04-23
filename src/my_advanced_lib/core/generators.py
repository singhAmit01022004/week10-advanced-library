from typing import Iterable, Generator


def process_data(data: Iterable[int]) -> Generator[int, None, None]:
    """Simple generator pipeline"""
    for item in data:
        yield item * 2