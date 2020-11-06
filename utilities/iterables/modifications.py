from typing import Iterable, Any
from itertools import islice


def to_chunks(iterable: Iterable[Any], chunk_size: int) -> Iterable:
    it = iter(iterable)
    item = list(islice(it, chunk_size))
    while item:
        yield item
        item = list(islice(it, chunk_size))
