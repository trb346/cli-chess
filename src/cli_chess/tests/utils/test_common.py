from cli_chess.utils.common import str_to_bool


def test_str_to_bool_truthy_strings():
    assert str_to_bool("true") is True
    assert str_to_bool("YES") is True
    assert str_to_bool("1") is True


def test_str_to_bool_falsy_strings():
    assert str_to_bool("false") is False
    assert str_to_bool("no") is False
    assert str_to_bool("0") is False
    assert str_to_bool("") is False


def test_str_to_bool_none_returns_false():
    # Missing config values surface as None; they must read as False,
    # not crash with an AttributeError traceback.
    assert str_to_bool(None) is False


def test_str_to_bool_non_string_returns_false():
    assert str_to_bool(1) is False
    assert str_to_bool(True) is False
