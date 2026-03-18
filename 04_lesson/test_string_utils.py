import pytest
from string_utils import StringUtils


string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str,expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    (" Skypro", "Skypro"),
    (" Hello world", "Hello world"),
    ("Python", "Python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

def test_contains_positive_false():
    assert string_utils.contains("Hello world", "W") == False

def test_contains_positive__false():
    assert string_utils.contains("Python", "u") == False

def test_contains_positive_true():
    assert string_utils.contains("Skypro", "S") == True
    

@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "S", "kypro"),
    ("Hello world", " world", "Hello"),
    ("Python", "h", "Pyton"),
])
def test_delete_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("  ", ""),
    ("", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

def test_trim_negative_none():
    with pytest.raises(AttributeError):
     assert string_utils.trim(None) == AttributeError

def test_contains_negative_a():
    with pytest.raises(AssertionError):
     assert string_utils.contains("", "W") == ""

def test_contains_negative_b():
    with pytest.raises(TypeError):
     assert string_utils.contains("Python", None) == "Python"

def test_contains_negative_c():
    with pytest.raises(AttributeError):
     assert string_utils.contains(None, "Hello") == AttributeError

def test_delete_negative():
    assert string_utils.delete_symbol("Python", "U") == "Python"

def test_delete__negative():
    with pytest.raises(AssertionError):
     assert string_utils.delete_symbol("SkyPro", " ")  == "Skypro"

def test_delete_negative_none():
    with pytest.raises(TypeError):
     assert string_utils.delete_symbol("SkyPro", None)  == "Skypro"