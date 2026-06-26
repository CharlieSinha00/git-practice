from main import subtract, multiply, divide
from greeting import greet

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_greet():
    assert greet("Alice") == "Hello and welcome, Alice!"
