from shopcalc.text_utils import slugify_text, truncate_text
""" 3 tests for the slugify function"""
def test_slugify_text():
    assert slugify_text("Hello World") == "hello-world"

def test_slugify_removes_special_characters():
    assert slugify_text("Hello, World!") == "hello-world"

def test_slugify_empty_string():
    assert slugify_text("")==""

"""3 tests for the truncate function"""
def test_truncate_text_shorter_than_max_length():
    assert truncate_text("Hello", 10) =="Hello" 

def test_truncate_text_longer_than_max_length():
    assert truncate_text("Hello, World!", 5) == "He..."

