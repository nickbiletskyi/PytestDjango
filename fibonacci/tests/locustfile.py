from locust import HttpUser, between, task


class FibonacciUser(HttpUser):
    """
    to run locust
    locust -f locustfile.py --host http://127.0.0.1:8000
    """

    # Wait time between each request (in seconds)
    wait_time = between(1, 2)

    @task
    def test_fibonacci(self):
        # Simulate a user making a GET request to the Fibonacci endpoint
        for n in range(1, 21):  # Testing Fibonacci for n from 1 to 20
            self.client.get(f"/fibonacci/", params={"n": n})
