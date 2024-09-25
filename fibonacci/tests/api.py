import json

import pytest

from django.test import Client
from django.urls import reverse

client = Client()

fibonacci_url = reverse("fibonacci")


@pytest.mark.parametrize("n, expected_f", [(0, 0), (1, 1), (20, 6765)])
def test_fibonacci_positive(time_tracker, client, n: int, expected_f: int) -> None:
    response = client.get(path=fibonacci_url, query_params={"n": n})
    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content["fibonacci"] == expected_f


@pytest.mark.parametrize(
    "n, expected_output",
    [
        ("hello", "Invalid input. 'n' must be an integer."),
        (-1, "n must be a non-negative integer."),
    ],
)
def test_fibonacci_negative(time_tracker, client, n: int, expected_output: str):
    response = client.get(path=fibonacci_url, query_params={"n": n})
    assert response.status_code == 400
    assert response.content.decode("utf-8") == expected_output
