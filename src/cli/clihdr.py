"""clihdr module."""

import subprocess

from multipledispatch import dispatch

from typehdr.listhdr import ListHdr
from typehdr.strhdr import StrHdr
from typehdr.jsonhdr import json_str_to_dict


@dispatch(list)
@json_str_to_dict
def runc(_cmd: list[str]) -> object:
    """
    Execute a command provided as a list of arguments.

    This overload expects the command to be supplied as a list of strings,
    where each element represents a single argument. The command is executed
    using :func:`subprocess.run` with output captured as text.

    The returned stdout is automatically post-processed by
    :func:`json_str_to_dict`, which converts JSON output into a Python object
    when possible.

    :param _cmd: Command and arguments to execute.
    :type _cmd: list[str]

    :return: Standard output of the executed command, or a parsed JSON object
             if the output is valid JSON.
    :rtype: object

    :raises subprocess.CalledProcessError: If the command exits with a
        non-zero status code.
    """
    result = subprocess.run(
        _cmd,
        capture_output=True,
        text=True,
        check=True,
    )

    return result.stdout


@dispatch(str)
@json_str_to_dict
def runc(_cmd: str) -> object:  # noqa: F811
    """
    Execute a command provided as a string.

    This overload accepts a single cmd string, which is split into arguments
    and processed using :class:`ListHdr` and :class:`StrHdr` to detect and
    preserve embedded strings (such as quoted arguments).

    The processed command is then executed using :func:`subprocess.run` with
    output captured as text.

    The returned stdout is automatically post-processed by
    :func:`json_str_to_dict`, which converts JSON output into a Python object
    when possible.

    :param _cmd: Command to execute as a single string.
    :type _cmd: str

    :return: Standard output of the executed command, or a parsed JSON object
             if the output is valid JSON.
    :rtype: object

    :raises subprocess.CalledProcessError: If the command exits with a
        non-zero status code.
    """
    _cmd = ListHdr.mutate(_cmd.split(), StrHdr.detect_embedded_str)

    result = subprocess.run(
        _cmd,
        capture_output=True,
        text=True,
        check=True,
    )

    return result.stdout
