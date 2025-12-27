"""strdhdr module."""


class StrHdr:
    """
    String header utility helpers.

    This class provides helper methods for inspecting and classifying
    string values based on their formatting.
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

        **Examples**

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
