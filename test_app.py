from app import hello_world, welcome_message

def test_hello_world():
    assert hello_world() == "Hello, DevOps!"

def test_return_type():
    assert isinstance(hello_world(), str)

def test_welcome_message_aaditya():
    assert welcome_message("Aaditya") == \
        "Welcome to DevOps, Aaditya!"

def test_welcome_message_john():
    assert welcome_message("John") == \
        "Welcome to DevOps, John!"
