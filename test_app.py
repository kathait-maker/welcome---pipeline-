from app import hello_world

def test_hello_world():
    assert hello_world() == "Hello, DevOps!"

def test_return_type():
    assert isinstance(hello_world(), str)
