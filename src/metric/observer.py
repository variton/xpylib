"""observer module."""

from functools import wraps


def measure(func: callable) -> callable:
    """
    Measure the execution time of a function.

    This decorator wraps a function and prints how long it took to execute,
    using :func:`time.perf_counter` for high-resolution timing.

    :param func: The function to be measured.
    :type func: Callable
    :return: A wrapped function with execution time measurement.
    :rtype: Callable

    **Example**

    .. code-block:: python

        @measure
        def slow_add(a, b) -> int:
            return a + b

        result = slow_add(2, 3)
        # Output:
        # slow_add executed in 0.000001 seconds
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapp function that measures execution time.

        :param args: Positional arguments passed to the wrapped function.
        :type args: tuple
        :param kwargs: Keyword arguments passed to the wrapped function.
        :type kwargs: dict
        :return: The return value of the wrapped function.
        :rtype: Any
        """
        start = __import__("time").perf_counter()
        result = func(*args, **kwargs)
        end = __import__("time").perf_counter()
        print(f"{func.__name__} executed in {end - start:.6f} seconds")
        return result

    return wrapper
