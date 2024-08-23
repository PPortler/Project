import pytest
from chain_of_responsibility import ConcreteHandler1, ConcreteHandler2, DefaultHandler

def test_concrete_handler1():
    handler1 = ConcreteHandler1()
    handler1.handle_request(1)
    with pytest.raises(AttributeError):
        handler1.handle_request(2)  # No next handler, should raise error

def test_concrete_handler2():
    handler2 = ConcreteHandler2()
    handler2.handle_request(2)
    with pytest.raises(AttributeError):
        handler2.handle_request(1)  # No next handler, should raise error

def test_default_handler():
    default_handler = DefaultHandler()
    default_handler.handle_request(3)
    default_handler.handle_request(4)

def test_chain_of_responsibility():
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    default_handler = DefaultHandler()

    handler1.set_next(handler2)
    handler2.set_next(default_handler)

    handler1.handle_request(1)  # Handled by ConcreteHandler1
    handler1.handle_request(2)  # Handled by ConcreteHandler2
    handler1.handle_request(3)  # Handled by DefaultHandler
    handler1.handle_request(4)  # Handled by DefaultHandler
