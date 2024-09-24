import pytest

from fibonacci.dynamic import dynamic_fibo_v2
from fibonacci.tests.conftest import track_performance

@pytest.mark.performance
@track_performance
def test_performance():
    dynamic_fibo_v2(1000)
