from abc import ABC, abstractmethod

class Handler(ABC):
    """Abstract Handler class for the Chain of Responsibility pattern."""

    @abstractmethod
    def handle_request(self, request):
        """Handles a request, optionally passing it to the next handler in the chain."""
        pass

    def set_next(self, handler):
        """Sets the next handler in the chain."""
        self.next_handler = handler

    def get_next(self):
        """Returns the next handler in the chain."""
        return self.next_handler

class ConcreteHandler1(Handler):
    """Concrete handler that handles requests of type 1."""

    def handle_request(self, request):
        if request == 1:
            print(f"ConcreteHandler1 handled request: {request}")
        else:
            if self.get_next():
                self.get_next().handle_request(request)

class ConcreteHandler2(Handler):
    """Concrete handler that handles requests of type 2."""

    def handle_request(self, request):
        if request == 2:
            print(f"ConcreteHandler2 handled request: {request}")
        else:
            if self.get_next():
                self.get_next().handle_request(request)

class DefaultHandler(Handler):
    """Default handler that handles all other requests."""

    def handle_request(self, request):
        print(f"DefaultHandler handled request: {request}")

# Test cases for the Chain of Responsibility pattern
def test_chain_of_responsibility():
    # Create handlers
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    default_handler = DefaultHandler()

    # Build the chain
    handler1.set_next(handler2)
    handler2.set_next(default_handler)

    # Test cases
    handler1.handle_request(1)  # Handled by ConcreteHandler1
    handler1.handle_request(2)  # Handled by ConcreteHandler2
    handler1.handle_request(3)  # Handled by DefaultHandler
    handler1.handle_request(4)  # Handled by DefaultHandler
