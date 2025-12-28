"""listhdr module."""


class ListHdr:
    """
    Utility class for performing header-like transformations on lists of strs.

    This class is designed as a namespace for static methods and is not
    intended to be instantiated.
    """

    @staticmethod
    def mutate(_data: list[str], _predicat: callable) -> list[str]:
        """
        Conditionally mutate elements of a list of strings.

        Iterates over the input list and applies a predicate function to
        each element. If the predicate evaluates to True for an element,
        the element is transformed by removing its first and last characters.
        Otherwise, the element is left unchanged.

        The original list is not modified; a new list is returned.

        Parameters
        ----------
        _data : list[str]
            A list of strings to be processed. If the list is empty,
            it is returned as-is.

        _predicat : callable
            A function that takes a single string argument and returns
            a boolean indicating whether the element should be mutated.

        Returns
        -------
        list[str]
            A new list of strings where elements satisfying the predicate
            have had their first and last characters removed.

        Notes
        -----
        - No validation is performed on string length. If the predicate
          returns True for strings shorter than two characters, the result
          will be an empty string.
        - The predicate is assumed to be side-effect free.

        Examples
        --------
        >>> ListHdr.mutate(["[abc]", "def"], lambda s: s.startswith("["))
        ['abc', 'def']

        >>> ListHdr.mutate([], lambda s: True)
        []
        """

        if len(_data) == 0:
            return _data

        l_data = []
        for element in _data:
            if _predicat(element):
                new_element = element[1:-1]
                l_data.append(new_element)
            else:
                l_data.append(element)
        return l_data
