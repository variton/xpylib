import json
import pytest

from typehdr.jsonhdr  import json_str_to_dict


def test_returns_none_when_func_returns_none():
    @json_str_to_dict
    def f():
        return None

    assert f() is None


def test_parses_json_string_result_to_python_object_dict():
    payload = {"a": 1, "b": "x"}

    @json_str_to_dict
    def f():
        return json.dumps(payload)

    assert f() == payload


def test_parses_json_string_result_to_python_object_list():
    payload = [1, 2, {"x": True}]

    @json_str_to_dict
    def f():
        return json.dumps(payload)

    assert f() == payload


def test_raises_type_error_when_result_is_not_str_or_none():
    @json_str_to_dict
    def f():
        return 123  # not None, not str

    with pytest.raises(TypeError) as excinfo:
        f()

    assert str(excinfo.value) == "Expected JSON string from f,got int"


def test_raises_type_error_includes_function_name_and_result_type_name():
    class Foo:
        pass

    @json_str_to_dict
    def myfunc():
        return Foo()

    with pytest.raises(TypeError) as excinfo:
        myfunc()

    assert str(excinfo.value) == "Expected JSON string from myfunc,got Foo"


def test_propagates_json_decode_error_for_invalid_json_string():
    @json_str_to_dict
    def f():
        return "{not valid json}"

    with pytest.raises(json.JSONDecodeError):
        f()


def test_passes_through_args_and_kwargs_to_wrapped_function():
    @json_str_to_dict
    def f(a, b=0, *, c=0):
        return json.dumps({"sum": a + b + c})

    assert f(1, 2, c=3) == {"sum": 6}


def test_preserves_wrapped_function_name_via_wraps():
    @json_str_to_dict
    def original_name():
        return json.dumps({"ok": True})
    
    l_var = original_name()
    assert original_name.__name__ == "original_name"
    assert l_var['ok'] == True
