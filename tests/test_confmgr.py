import json
import pytest

from pathlib import Path

from config.confmgr import ConfMgr


def test_load_valid_json(tmp_path: Path):
    config = {"a": 1, "b": "test"}
    config_file = tmp_path / "config.json"

    config_file.write_text(json.dumps(config))

    result = ConfMgr.load(str(config_file))

    assert result == config


def test_load_file_not_found(tmp_path: Path):
    missing_file = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError) as excinfo:
        ConfMgr.load(str(missing_file))

    assert str(excinfo.value) == f"File '{missing_file}' not found"


def test_load_invalid_json(tmp_path: Path):
    invalid_file = tmp_path / "bad.json"
    invalid_file.write_text("{ invalid json }")

    with pytest.raises(ValueError) as excinfo:
        ConfMgr.load(str(invalid_file))

    assert str(excinfo.value) == f"File '{invalid_file}' is not a valid JSON"
