import pytest

from fibonacci.fib_cached import fibonacci_cached
from fibonacci.fib_cached import fibonacci_lru_cached
from fibonacci.naive import fibonacci_naive
from typing import Callable
from fixtures import time_tracker
from fibonacci.dynamic import dynamic_fibo


@pytest.mark.parametrize(
    "fib_func", [dynamic_fibo, fibonacci_naive, fibonacci_cached, fibonacci_lru_cached]
)
@pytest.mark.parametrize("n, expected_f", [(0, 0), (1, 1), (20, 6765)])
def test_fibonacci(time_tracker, fib_func: Callable, n: int, expected_f: int) -> None:
    res = fib_func(n)
    assert res == expected_f
