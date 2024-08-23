from abc import ABC, abstractmethod

class Handler(ABC):
    """Abstract Handler class for the Chain of Responsibility pattern."""
    _next_handler = None

    def set_next(self, handler):
        """Sets the next handler in the chain."""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        """Handles the request if applicable. If not, passes it to the next handler."""
        pass

class ConcreteHandler1(Handler):
    """Concrete handler that handles specific requests."""
    def handle(self, request):
        if request == "Request 1":
            print(f"ConcreteHandler1 handling request: {request}")
            return True
        else:
            if self._next_handler is not None:
                return self._next_handler.handle(request)
            else:
                print(f"No handler found for request: {request}")

class ConcreteHandler2(Handler):
    """Concrete handler that handles specific requests."""
    def handle(self, request):
        if request == "Request 2":
            print(f"ConcreteHandler2 handling request: {request}")
            return True
        else:
            if self._next_handler is not None:
                return self._next_handler.handle(request)
            else:
                print(f"No handler found for request: {request}")

# Testing using Pytest
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
    assert handler1.handle("Request 3") == None
