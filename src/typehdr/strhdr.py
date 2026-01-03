"""strdhdr module."""


class StrHdr:
    r"""
    String header utility helpers.

    This class provides helper methods for inspecting and classifying
    string values based on their formatting.

    **Examples: detect_embedded_str**

    .. code-block:: python

        StrHdr.detect_embedded_str('"hello"')
        # True

        StrHdr.detect_embedded_str("'world'")
        # True

        StrHdr.detect_embedded_str("hello")
        # False

        StrHdr.detect_embedded_str("")
        # False

        StrHdr.detect_embedded_str('"mismatch\'')
        # False
    """

    @staticmethod
    def detect_embedded_str(_s: str) -> bool:
        r"""
        Detect whether a string is enclosed in matching quotation marks.

        A string is considered an *embedded string* if **all** of the following
        conditions are met:

        - The string is not empty
        - The first and last characters are identical
        - The matching characters are either a single quote (``'``)
          or a double quote (``"``)

        :param _s: The input string to inspect.
        :type _s: str
        :return: ``True`` if the string is wrapped in matching quotes,
                 otherwise ``False``.
        :rtype: bool


        **Notes**

        - Empty strings safely return ``False``.
        - Escape sequences are not interpreted.
        - Nested or mixed quotation marks are not supported.
        """
        QUOTES = ['"', "'"]
        if isinstance(_s, str) and len(_s) != 0:
            for quote in QUOTES:
                if _s.count(quote) == 2:
                    return True
            return False
        return False

    @staticmethod
    def str_to_list(_s: str) -> list[str]:
        r"""
        Convert a whitespace-separated string into a list of strings.

        This method splits the input string on any whitespace and returns
        a list containing each resulting substring. Consecutive whitespace
        characters are treated as a single separator.

        :param _s: Input string to be split.
        :type _s: str
        :return: A list of substrings extracted from the input string.
        :rtype: list[str]

        **Examples**

        Basic usage:

        >>> StrHdr.str_to_list("hello world")
        ['hello', 'world']

        Multiple spaces and tabs are handled automatically:

        >>> StrHdr.str_to_list("one   two\\tthree")
        ['one', 'two', 'three']

        Leading and trailing whitespace is ignored:

        >>> StrHdr.str_to_list("  spaced words  ")
        ['spaced', 'words']

        Empty string returns an empty list:

        >>> StrHdr.str_to_list("")
        []
        """
        return _s.split()
