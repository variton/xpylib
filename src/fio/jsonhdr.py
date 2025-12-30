"""jsonhdr module."""

import json

"""
json_hdr
========

Small helper utilities for reading and writing JSON files.

The :class:`~json_hdr.JsonHdr` class wraps JSON serialization/deserialization
with UTF-8 encoding and raises common exceptions (missing file, invalid JSON,
non-serializable data) with preserved context.

Examples
--------

Read JSON from a file:

.. code-block:: python

    from json_hdr import JsonHdr

    hdr = JsonHdr("data.json")
    data = hdr.read()
    print(data)

Write JSON to a file:

.. code-block:: python

    from json_hdr import JsonHdr

    hdr = JsonHdr("out.json")
    hdr.write({"hello": "world"})
"""


class JsonHdr:
    """
    JSON file reader and writer.

    This class provides a minimal interface to:

    - read JSON from a file into Python objects
    - write JSON-serializable Python objects to a file

    Parameters
    ----------
    _filepath:
        Path to the JSON file.

    Examples
    --------

    Basic write + read round-trip:

    .. code-block:: python

        from json_hdr import JsonHdr

        hdr = JsonHdr("example.json")
        hdr.write({"a": 1, "b": [1, 2, 3]})
        data = hdr.read()
        assert data["a"] == 1
        assert data["b"] == [1, 2, 3]

    Handling invalid JSON (raises :class:`ValueError`):

    .. code-block:: python

        # Suppose "broken.json" contains: { invalid json
        from json_hdr import JsonHdr

        hdr = JsonHdr("broken.json")
        try:
            hdr.read()
        except ValueError as e:
            print("Invalid JSON:", e)

    Handling missing files (raises :class:`FileNotFoundError`):

    .. code-block:: python

        from json_hdr import JsonHdr

        hdr = JsonHdr("does_not_exist.json")
        try:
            hdr.read()
        except FileNotFoundError as e:
            print("Missing file:", e)

    Writing non-serializable objects (raises :class:`TypeError`):

    .. code-block:: python

        from json_hdr import JsonHdr

        hdr = JsonHdr("out.json")
        try:
            hdr.write({"bad": {1, 2, 3}})  # sets are not JSON-serializable by default
        except TypeError as e:
            print("Not serializable:", e)
    """

    def __init__(self, _filepath):
        """
        Initialize the JSON handler.

        :param _filepath: Path to the JSON file.
        :type _filepath: str
        """
        self.filepath_ = _filepath

    def read(self) -> object:
        """
        Read and deserialize JSON data from the file.

        Opens the file specified by ``filepath_`` and parses its contents
        into a Python object.

        :returns: Parsed JSON data (e.g., ``dict``, ``list``).
        :rtype: object

        :raises FileNotFoundError: If the file does not exist or cannot be opened.
        :raises ValueError: If the file contains invalid JSON.
        """
        try:
            with open(self.filepath_, "r", encoding="utf-8") as f:
                l_data = json.load(f)
                return l_data
        except FileNotFoundError as e:
            raise FileNotFoundError(f"{str(e)}") from e
        except ValueError as e:
            raise ValueError(f"{str(e)}") from e

    def write(self, _data: object, _options: object = None) -> None:
        """
        Serialize and write data to a JSON file.

        Writes the provided Python object to the file specified by
        ``filepath_`` using UTF-8 encoding and formatted output
        (indentation of 4 spaces, ``ensure_ascii=False``).

        The ``_object`` parameter is currently unused and reserved for
        future extensions.

        :param _data: JSON-serializable Python object (e.g., ``dict``, ``list``).
        :type _data: object
        :param _object: Reserved for future use (currently unused).
        :type _object: Any, optional

        :raises FileNotFoundError: If the file path is invalid or inaccessible.
        :raises TypeError: If ``_data`` is not JSON-serializable.
        """
        try:
            with open(self.filepath_, "w", encoding="utf-8") as f:
                json.dump(_data, f, indent=4, ensure_ascii=False)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"{str(e)}") from e
        except TypeError as e:
            raise TypeError(f"{str(e)}") from e
