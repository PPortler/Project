import pytest
from chain_of_responsibility import ConcreteHandler1, ConcreteHandler2, Handler

def test_chain_of_responsibility():
    # Create the chain of handlers
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler1.set_next(handler2)

    # Test request 1
    assert handler1.handle("Request 1") == True

    # Test request 2
    assert handler1.handle("Request 2") == True

    # Test an unknown request
    assert handler1.handle("Request 3") == False

def test_no_handler():
    # Create a single handler
    handler1 = ConcreteHandler1()

    # Test an unknown request
    assert handler1.handle("Request 3") == False
