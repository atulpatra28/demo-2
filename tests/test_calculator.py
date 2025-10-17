from app.calculator import add, subtract

def test_add():
    assert add(1, 3) == 4

def test_subtract():
    assert subtract(7, 3) == 4
