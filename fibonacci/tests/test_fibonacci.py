import pytest

from fibonacci.fib_cached import fibonacci_cached
from fibonacci.fib_cached import fibonacci_lru_cached
from fibonacci.naive import fibonacci_naive
from typing import Callable


@pytest.mark.parametrize(
    "fib_func", [fibonacci_naive, fibonacci_cached, fibonacci_lru_cached]
)
@pytest.mark.parametrize("n, expected_f", [(0, 0), (1, 1), (20, 6765)])
def test_fibonacci(fib_func: Callable, n: int, expected_f: int) -> None:
    res = fib_func(n)
    assert res == expected_f
