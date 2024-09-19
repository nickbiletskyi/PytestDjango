import pytest

from fibonacci.dynamic import dynamic_fibo_v2
from typing import Callable
from datetime import datetime, timedelta
from conftest import track_performance

@pytest.mark.performance
@track_performance
def test_performance():
    dynamic_fibo_v2(1000)
