from typing import Callable

import pytest

from datetime import datetime, timedelta


@pytest.fixture
def time_tracker():
    start = datetime.now()
    yield
    end = datetime.now()
    diff = end - start
    print(f" runtime: {diff.total_seconds()} sec")


class PerformanceException(Exception):
    def __init__(self, runtime: timedelta, limit: timedelta):
        self.runtime = runtime
        self.limit = limit

    def __str__(self) -> str:
        return f"Performance test failed, runtime: {self.runtime.total_seconds()}, limit: {self.limit.total_seconds()}"


def track_performance(method: Callable, runtime_limit=timedelta(seconds=2)):
    def run_function_and_validate_runtime(*args, **kwargs):
        start = datetime.now()
        result = method(*args, **kwargs)
        end = datetime.now()
        runtime = end - start
        print(f"runtime: {runtime.total_seconds()} sec")

        if runtime > runtime_limit:
            raise PerformanceException(runtime=runtime, limit=runtime_limit)

        return result

    return run_function_and_validate_runtime
