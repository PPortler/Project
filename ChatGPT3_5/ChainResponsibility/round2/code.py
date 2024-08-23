from abc import ABC, abstractmethod

# Base Handler class for Chain of Responsibility
class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        """Set the next handler in the chain."""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        """Handle the request. To be implemented by concrete handlers."""
        pass


# Concrete Handlers
class ConcreteHandlerA(Handler):
    def handle(self, request):
        """Process the request in Handler A and pass to next if available."""
        print(f"Handler A processing request: {request}")
        if self._next_handler:
            self._next_handler.handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        """Process the request in Handler B and pass to next if available."""
        print(f"Handler B processing request: {request}")
        if self._next_handler:
            self._next_handler.handle(request)


# Base Handler Decorator
class HandlerDecorator(Handler):
    def __init__(self, handler):
        super().__init__()
        self._handler = handler

    def set_next(self, handler):
        """Set the next handler in the chain for the decorator."""
        self._handler.set_next(handler)
        return handler

    def handle(self, request):
        """Delegate the handling to the decorated handler."""
        self._handler.handle(request)


# Concrete Decorators
class LoggingDecorator(HandlerDecorator):
    def handle(self, request):
        """Log the request before passing it to the next handler."""
        print(f"Logging request: {request}")
        super().handle(request)


class UppercaseDecorator(HandlerDecorator):
    def handle(self, request):
        """Convert the request to uppercase and then pass it to the next handler."""
        request = request.upper()
        super().handle(request)


# Main function to demonstrate functionality
def main():
    # Create concrete handlers
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()

    # Set up the chain of responsibility
    handler_a.set_next(handler_b)

    # Decorate handlers with logging and uppercase functionality
    decorated_handler_a = LoggingDecorator(UppercaseDecorator(handler_a))

    # List of requests to process
    requests = ["request 1", "request 2"]
    for request in requests:
        decorated_handler_a.handle(request)


if __name__ == "__main__":
    main()
