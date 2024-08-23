from abc import ABC, abstractmethod


class Handler(ABC):
    """Abstract Handler class."""

    @abstractmethod
    def handle_request(self, request):
        pass


class ConcreteHandler1(Handler):
    """Concrete handler 1."""

    def handle_request(self, request):
        if request == "A":
            print("Handler 1 processed request A.")
            return True
        else:
            return False


class ConcreteHandler2(Handler):
    """Concrete handler 2."""

    def handle_request(self, request):
        if request == "B":
            print("Handler 2 processed request B.")
            return True
        else:
            return False


class DefaultHandler(Handler):
    """Default handler."""

    def handle_request(self, request):
        print("Default handler processed request.")
        return True


class ChainOfResponsibility:
    """Chain of Responsibility pattern implementation."""

    def __init__(self):
        self._handlers = []

    def add_handler(self, handler: Handler):
        """Adds a handler to the chain."""
        self._handlers.append(handler)

    def handle_request(self, request):
        """Processes the request through the chain."""
        for handler in self._handlers:
            if handler.handle_request(request):
                return

        # No handler found, reach the default handler
        DefaultHandler().handle_request(request)


# Test cases
def test_chain_of_responsibility():
    chain = ChainOfResponsibility()
    chain.add_handler(ConcreteHandler1())
    chain.add_handler(ConcreteHandler2())

    # Test case 1: request A
    chain.handle_request("A")
    # Expected output: Handler 1 processed request A.

    # Test case 2: request B
    chain.handle_request("B")
    # Expected output: Handler 2 processed request B.

    # Test case 3: request C (no handler)
    chain.handle_request("C")
    # Expected output: Default handler processed request.
