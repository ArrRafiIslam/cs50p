from hello_w5 import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Rafi") == "hello, Rafi"

# [python -m pytest folder_name/] ---> to run pytest in folder