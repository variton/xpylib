"""jsonhdr module."""

from functools import wraps


def json_str_to_dict(func: callable) -> callable:
    """
    Decorate to convert a JSON string returned by a function into a dict.

    This decorator wraps a function that is expected to return a JSON-formatted
    string. It parses the JSON string and returns a dictionary. If the wrapped
    function returns None, None is returned. If the result is not a string,
    a TypeError is raised.

    Parameters
    ----------
    func : callable
        The function to wrap. It should return a JSON-formatted string.

    Returns
    -------
    callable
        The wrapped function, which returns a dict or None.

    Raises
    ------
    TypeError
        If the wrapped function does not return a string or None.
    json.JSONDecodeError
        If the returned string is not valid JSON.

    Examples
    --------
    >>> @json_str_to_dict
    ... def get_json():
    ...     return '{"a": 1, "b": 2}'
    ...
    >>> get_json()
    {'a': 1, 'b': 2}

    >>> @json_str_to_dict
    ... def get_none():
    ...     return None
    ...
    >>> get_none() is None
    True
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if result is None:
            return None

        if isinstance(result, str):
            return __import__("json").loads(result)

        l_fname = func.__name__
        l_rname = type(result).__name__

        raise TypeError(f"Expected JSON string from {l_fname},got {l_rname}")

    return wrapper
