import os
import tempfile
import pytest

from fs.fsmgr import FsMgr

@pytest.fixture
def tmp_structure(tmp_path):
    # tmp_path is a pathlib.Path, we need native string sometimes
    # Create files and directories
    dir1 = tmp_path / "dir1"
    dir1.mkdir()
    file1 = dir1 / "file1.txt"
    file1.write_text("test")
    file2 = tmp_path / "file2.txt"
    file2.write_text("test2")
    dir2 = tmp_path / "dir2"
    dir2.mkdir()
    return tmp_path

def test_get_absolute_path_found_file(tmp_structure):
    # Create file
    expected_path = tmp_structure / "file2.txt"
    result = FsMgr.get_absolute_path("file2.txt", str(tmp_structure))
    assert result == str(expected_path.resolve())

def test_get_absolute_path_found_directory(tmp_structure):
    expected_path = tmp_structure / "dir1"
    result = FsMgr.get_absolute_path("dir1", str(tmp_structure))
    assert result == str(expected_path.resolve())

def test_get_absolute_path_not_found(tmp_structure):
    with pytest.raises(FileNotFoundError) as excinfo:
        FsMgr.get_absolute_path("nonexistent.txt", str(tmp_structure))
    assert "nonexistent.txt" in str(excinfo.value)

def test_get_absolute_path_name_found_file(tmp_structure):
    file1 = tmp_structure / "dir1" / "file1.txt"
    result = FsMgr.get_absolute_path_name("file1.txt", str(tmp_structure))
    assert result == str((tmp_structure / "dir1").resolve())

def test_get_absolute_path_name_found_directory(tmp_structure):
    result = FsMgr.get_absolute_path_name("dir2", str(tmp_structure))
    assert result == str(tmp_structure.resolve())

def test_get_absolute_path_name_not_found(tmp_structure):
    with pytest.raises(FileNotFoundError) as excinfo:
        FsMgr.get_absolute_path_name("doesnotexist", str(tmp_structure))
    assert "doesnotexist" in str(excinfo.value)

def test_get_absolute_paths_found_some(tmp_structure):
    # file1.txt is inside dir1, file2.txt and dir2 are in root tmp_structure
    found, paths = FsMgr.get_absolute_paths(
        str(tmp_structure), "file1.txt", "file2.txt", "dir2", "notfound"
    )
    absolute_paths = set(map(str, [
        tmp_structure / "dir1" / "file1.txt",
        tmp_structure / "file2.txt",
        tmp_structure / "dir2"
    ]))
    assert found is True
    assert set(paths) == absolute_paths or set(map(os.path.abspath, paths)) == absolute_paths

def test_get_absolute_paths_found_none(tmp_structure):
    found, paths = FsMgr.get_absolute_paths(str(tmp_structure), "nope1", "nope2")
    assert found is False
    assert paths == []

def test_get_absolute_paths_empty_args(tmp_structure):
    found, paths = FsMgr.get_absolute_paths(str(tmp_structure))
    assert found is False
    assert paths == []
