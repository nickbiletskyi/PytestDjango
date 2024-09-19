from django.http import JsonResponse, HttpResponseBadRequest
from fibonacci.dynamic import dynamic_fibo_v2 # Import the Fibonacci function


def fibonacci_view(request):
    try:
        # Extract the 'n' parameter from the GET request
        n = int(request.GET.get('n'))
        if n < 0:
            return HttpResponseBadRequest("n must be a non-negative integer.")

        # Calculate the Fibonacci number
        result = dynamic_fibo_v2(n)

        # Return the result as JSON
        return JsonResponse({"n": n, "fibonacci": result})
    except (TypeError, ValueError):
        return HttpResponseBadRequest("Invalid input. 'n' must be an integer.")
