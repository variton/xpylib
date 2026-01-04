import json
import pytest

from fio.jsonmgr import JsonMgr  # adjust import to your module name/path


def test_write_and_read_round_trip(tmp_path):
    p = tmp_path / "data.json"
    mgr = JsonMgr(str(p))

    payload = {"a": 1, "b": [1, 2, 3], "c": {"nested": True}}
    mgr.write(payload)

    loaded = mgr.read()
    assert loaded == payload


def test_write_unicode_preserves_characters(tmp_path):
    p = tmp_path / "unicode.json"
    mgr = JsonMgr(str(p))

    payload = {"text": "café — 你好 — 🚀"}
    mgr.write(payload)

    # Verify the raw file contains unicode (ensure_ascii=False)
    raw = p.read_text(encoding="utf-8")
    assert "café" in raw
    assert "你好" in raw
    assert "🚀" in raw

    # And it still reads back correctly
    loaded = mgr.read()
    assert loaded == payload


def test_read_missing_file_raises(tmp_path):
    p = tmp_path / "missing.json"
    mgr = JsonMgr(str(p))

    with pytest.raises(FileNotFoundError):
        mgr.read()


def test_read_invalid_json_raises_value_error(tmp_path):
    p = tmp_path / "broken.json"
    p.write_text("{ invalid json", encoding="utf-8")
    mgr = JsonMgr(str(p))

    with pytest.raises(ValueError):
        mgr.read()


def test_write_non_serializable_raises_type_error(tmp_path):
    p = tmp_path / "out.json"
    mgr = JsonMgr(str(p))

    # sets aren't JSON-serializable by default
    payload = {"bad": {1, 2, 3}}

    with pytest.raises(TypeError):
        mgr.write(payload)


def test_write_creates_file(tmp_path):
    p = tmp_path / "created.json"
    mgr = JsonMgr(str(p))

    mgr.write({"ok": True})

    assert p.exists()
    # sanity check it is valid JSON
    assert json.loads(p.read_text(encoding="utf-8")) == {"ok": True}
