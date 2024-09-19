import pytest

from datetime import datetime


@pytest.fixture
def time_tracker():
    start = datetime.now()
    yield
    end = datetime.now()
    diff = end - start
    print(f"runtime: {diff.total_seconds()} seconds")
