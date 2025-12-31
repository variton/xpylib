"""confmgr module."""

from fio.jsonhdr import JsonHdr


class ConfMgr:
    """
    Load configuration data from a JSON file.

    The :class:`ConfMgr` class provides a simple interface for reading
    configuration data from a JSON file. It delegates JSON parsing to
    ``JsonHdr`` and normalizes common error messages.

    Examples
    --------
    Load a valid JSON configuration file::

        from confmgr import ConfMgr

        config = ConfMgr.load("/etc/myapp/config.json")
        print(config)

    Example output::

        {'host': 'localhost', 'port': 8080}

    Handle a missing configuration file::

        from confmgr import ConfMgr

        try:
            ConfMgr.load("/path/to/missing.json")
        except FileNotFoundError as exc:
            print(exc)

    Output::

        File '/path/to/missing.json' not found

    Handle invalid JSON content::

        from confmgr import ConfMgr

        try:
            ConfMgr.load("/path/to/invalid.json")
        except ValueError as exc:
            print(exc)

    Output::

        File '/path/to/invalid.json' is not a valid JSON
    """

    @staticmethod
    def load(_filepath: str) -> object:
        """
        Load the configuration from the specified JSON file.

        Parameters
        ----------
        _filepath : str
            Absolute path to the JSON configuration file.

        Returns
        -------
        Any
            The loaded configuration data.

        Raises
        ------
        FileNotFoundError
            If the specified configuration file does not exist.
        ValueError
            If the file content is not valid JSON.
        """
        try:
            l_json_hdr = JsonHdr(_filepath)
            l_config = l_json_hdr.read()
            return l_config
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File '{_filepath}' not found") from e
        except ValueError as e:
            raise ValueError(f"File '{_filepath}' is not a valid JSON") from e
