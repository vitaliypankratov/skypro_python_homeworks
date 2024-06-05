import pytest
from string_utils import StringUtils

utils = StringUtils()
# CAPITALIZE

def test_capitalize():
    # Positive tests
    assert utils.capitalize("posuda") == "Posuda"
    assert utils.capitalize("mukomol") == "Mukomol"
    assert utils.capitalize("123") == "123"

    # Negative tests
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("12345") == "12345"

# TRIM

def test_trim():
    # Positive tests
    assert utils.trim("    Kulak") == "Kulak"
    assert utils.trim("  Upravdom  ") == "Upravdom  "
    assert utils.trim("  TAHTA  ") == "TAHTA  "

    # Negative tests
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim("12345") == "12345"

@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim("  TAHTA  ") == "  TAHTA  "

# TO_LIST

@pytest.mark.parametrize('string, delimeter, result', [
    # Positive tests
    ("конь,собака,кошечка", ",", ["конь", "собака", "кошечка"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("*@$@%@&", "@", ["*", "$", "%", "&"]),
    # Negative tests
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
])    


def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else: res = utils.to_list(string, delimeter)
    assert res == result

# CONTAINS

@pytest.mark.parametrize('string, symbol, result', [

    ("кишка", "к", True),
    (" лось", "о", True),
    ("трюмо ", "р", True),
    ("царь-пушка", "-", True),
    ("999", "9", True),
    ("", "", True),
    ("Кишка", "А", False),
    ("кардон", "г", False),
    ("номер", "№", False),
    ("", "f", False),
    ("12", "я", False)

])

def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

# DELETE_SYMBOL

@pytest.mark.parametrize('string, symbol, result', [

    ("кот", "к", "от"),
    ("Лось", "о", "Лсь"),
    ("Трюмо", "Т", "рюмо"),
    ("123", "1", "23"),
    ("Пётр Первый", " ", "ПётрПервый"),
    ("бинокль", "з", "бинокль"),
    ("", "ц", ""),
    ("", "", ""),
    ("кардон", "", "кардон"),
    ("номер", " ", "номер"),
])

def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

# STARTS_WITH

@pytest.mark.parametrize('string, symbol, result', [

    ("кинжал", "к", True),
    ("", "", True),
    ("Трюмо", "Т", True),
    ("Limon", "L", True),
    ("Когда-то", "К", True),
    ("126", "1", True),

    ("Кишка", "к", False),
    ("кардон", "К", False),
    ("", "%", False),
    ("картошка", "ж", False)

])

def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

# END_WITH

@pytest.mark.parametrize('string, symbol, result', [

    ("Кинжал", "л", True),
    ("КАШПО", "О", True),
    ("", "", True),
    ("Limon", "n", True),
    ("125", "5", True),
    ("ZIG-ZAg", "g", True),
    ("лесниК", "К", True),

    ("Кишка", "к", False),
    ("ваниль", "Ь", False),
    ("ШЕРСТЬ", " ", False),
    ("", "*", False),
    ("картошка", "6", False)

])

def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

# IS_EMPTY

@pytest.mark.parametrize('string, result', [

    ("", True),
    (" ", True),
    ("  ", True),

    ("не пусто", False),
    ("не пусто с пробелом", False),
    ("7575",  False)

])

def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

# LIST_TO_STRING

@pytest.mark.parametrize('lst, joiner, result', [
    (["j", "o", "b"], ",", "j,o,b"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    (["человек", "слон"], "-", "человек-слон"),
    (["человек", "слон"], "синий", "человексинийслон"),
    (["l", "o", "l"], "", "lol"),
    ([], None, ""),
    ([], ",", ""),
    ([], "чёлка", "")
])

def test_list_to_string(lst, joiner, result):
    if joiner is None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result