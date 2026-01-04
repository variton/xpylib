"""jsonhdr module.

This module provides a minimal JSON file reader and writer.
"""

import json


class JsonMgr:
    r"""
    JSON file reader and writer.

    This class provides a minimal interface to:

    - read JSON from a file into Python objects
    - write JSON-serializable Python objects to a file

    :param _filepath: Path to the JSON file.
    :type _filepath: str

    **Examples**

    Basic write + read round-trip::

        from jsonmgr import JsonMgr

        mgr = JsonMgr("example.json")
        mgr.write({"a": 1, "b": [1, 2, 3]})
        data = mgr.read()

        assert data["a"] == 1
        assert data["b"] == [1, 2, 3]

    Handling invalid JSON (raises :class:`ValueError`)::

        # Suppose "broken.json" contains: { invalid json
        from jsonmgr import JsonMgr

        mgr = JsonMgr("broken.json")
        try:
            mgr.read()
        except ValueError as e:
            print("Invalid JSON:", e)

    Handling missing files (raises :class:`FileNotFoundError`)::

        from jsonmgr import JsonMgr

        mgr = JsonMgr("does_not_exist.json")
        try:
            mgr.read()
        except FileNotFoundError as e:
            print("Missing file:", e)

    Writing non-serializable objects (raises :class:`TypeError`)::

        from jsonmgr import JsonMgr

        mgr = JsonMgr("out.json")
        try:
            mgr.write({"bad": {1, 2, 3}})  # sets are not JSON-serializable
        except TypeError as e:
            print("Not serializable:", e)
    """

    def __init__(self, _filepath: str):
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

        :returns: Parsed JSON data (e.g., ``dict`` or ``list``).
        :rtype: object

        :raises FileNotFoundError: If the file does not exist
        :raises FileNotFoundError: If the file cannot be opened.
        :raises ValueError: If the file contains invalid JSON.
        """
        try:
            with open(self.filepath_, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(str(e)) from e
        except ValueError as e:
            raise ValueError(str(e)) from e

    def write(self, _data: object, _options: object | None = None) -> None:
        """
        Serialize and write data to a JSON file.

        Writes the provided Python object to the file specified by
        ``filepath_`` using UTF-8 encoding and formatted output.

        - Indentation: 4 spaces
        - ``ensure_ascii=False``

        The ``_options`` parameter is currently unused and reserved
        for future extensions.

        :param _data: JSON-serializable Python object.
        :type _data: object
        :param _options: Reserved for future use.
        :type _options: object, optional

        :raises FileNotFoundError: If the file path is invalid or inaccessible.
        :raises TypeError: If ``_data`` is not JSON-serializable.
        """
        try:
            with open(self.filepath_, "w", encoding="utf-8") as f:
                json.dump(_data, f, indent=4, ensure_ascii=False)
        except FileNotFoundError as e:
            raise FileNotFoundError(str(e)) from e
        except TypeError as e:
            raise TypeError(str(e)) from e
