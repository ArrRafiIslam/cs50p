# Unit Tests
'''
from calculator_w5 import square
def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()
'''

# Assert
'''
from calculator_w5 import square
def main():
    test_square()
def test_square():
    assert square(2) == 4
    assert square(3) == 9

if __name__ == "__main__":
    main()
'''

'''
from calculator_w5 import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared is not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared is not 0")

if __name__ == "__main__":
    main()
'''

# pytest
# [python -m pytest filename.py] ---> to run code
'''
from calculator_w5 import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
'''
'''
from calculator_w5 import square
import pytest

def test_postivie():
    assert square(2) == 4
    assert square(3) == 9

def test_negetive():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

'''

# Testing Strings
'''
from hello_w5 import hello

def test_hello():
    assert hello("Rafi") == "hello, Rafi"
    assert hello() == "hello, world"
'''

'''
from hello_w5 import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Rafi") == "hello, Rafi"
'''

'''
from hello_w5 import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
'''

# Organizing Tests in Folder





































































































































