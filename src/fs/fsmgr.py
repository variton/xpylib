"""fsmgr module."""

import os


class FsMgr:
    r"""
    Filesystem utility manager providing helper methods to locate files.

    and directories by name within a given base directory.
    This class offers static methods to:

    - Resolve the absolute path of a file or directory by name.
    - Resolve the absolute path of the parent directory containing a given
      file or directory.
    - Resolve absolute paths for multiple files or directories in a single
      operation.

    All searches are performed recursively starting from a specified base
    directory using :func:`os.walk`. The class is stateless and intended to be
    used as a pure utility without instantiation.

    .. note::
       These methods may be expensive on large directory trees, as they
       traverse the filesystem recursively.

    .. seealso::
       :mod:`os`
       :func:`os.walk`
       :func:`os.path.abspath`
    """

    @staticmethod
    def get_absolute_path(_nodename: str, _base_dir: str = ".") -> str:
        """
        Get the absolute path of a specified file.

        under the base directory.

        :param _nodename: Name of the file or directory to search for.
        :type _nodename: str
        :param _base_dir: Directory to start search from. Defaults to current
                          directory.
        :type _base_dir: str, optional
        :return: Absolute path to the file or directory if found.
        :rtype: str
        :raises FileNotFoundError: If the file or directory cannot be found.

        :Example:

        .. code-block:: python

           abs_path = FsMgr.get_absolute_path("test.txt", "/tmp")
           print(abs_path)  # Outputs absolute path to test.txt

        """
        l_base_dir = os.path.abspath(_base_dir)

        for root, directories, files in os.walk(l_base_dir):
            if _nodename in files or _nodename in directories:
                l_file_path = os.path.join(root, _nodename)
                return os.path.abspath(l_file_path)

        raise FileNotFoundError(f"File {_nodename} not found in {l_base_dir}")

    @staticmethod
    def get_absolute_path_name(_nodename: str, _base_dir: str = ".") -> str:
        """
        Get the absolute path of the given file under the base directory.

        :param _nodename: Name of the file or directory to search for.
        :type _nodename: str
        :param _base_dir: Directory to start search from. Defaults to current
                          directory.
        :type _base_dir: str, optional
        :return: Absolute path to the parent directory containing the file or
                 directory.
        :rtype: str
        :raises FileNotFoundError: If the file or directory cannot be found.

        :Example:

        .. code-block:: python

           parent_dir = FsMgr.get_absolute_path_name("data.csv", "/var/data")
           print(parent_dir)  # Outputs path containing data.csv

        """
        l_base_dir = os.path.abspath(_base_dir)

        for root, directories, files in os.walk(l_base_dir):
            if _nodename in files or _nodename in directories:
                return root

        raise FileNotFoundError(f"File {_nodename} not found in {l_base_dir}")

    @staticmethod
    def get_absolute_paths(_base_dir: str, *args) -> tuple[bool, list[str]]:
        """
        Get the absolute paths for multiple files.

        :param _base_dir: Directory to start search from.
        :type _base_dir: str
        :param args: Names of files or directories to search for.
        :type args: str
        :return: Tuple (has_paths, path_dir_list) where has_paths is True if at
                 least one path was found, and path_dir_list is a list of
                 absolute paths.
        :rtype: tuple[bool, list[str]]

        :Example:

        .. code-block:: python

           found, paths = FsMgr.get_absolute_paths(
               "/home/user", "file1.txt", "dir2"
           )
           if found:
               print(paths)  # List of absolute paths found

        """
        l_base_dir = os.path.abspath(_base_dir)
        l_path_dir_list = []
        l_has_paths = False
        for ielement in args:
            for root, directories, files in os.walk(l_base_dir):
                if ielement in directories or ielement in files:
                    l_file_path = os.path.join(root, ielement)
                    l_path_dir_list.append(l_file_path)
                    l_has_paths = True

        return l_has_paths, l_path_dir_list
