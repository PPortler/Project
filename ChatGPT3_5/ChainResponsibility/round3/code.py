import logging
from abc import ABC, abstractmethod

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger()

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

    def get_output(self, request):
        """Method to get output for the given request."""
        output = []
        self._output = output
        self.handle(request)
        return "\n".join(output)


# Concrete Handlers
class ConcreteHandlerA(Handler):
    def handle(self, request):
        """Process the request in Handler A and pass to next if available."""
        logger.info(f"Handler A processing request: {request}")
        if self._next_handler:
            self._next_handler.handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        """Process the request in Handler B and pass to next if available."""
        logger.info(f"Handler B processing request: {request}")
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
        logger.info(f"Logging request: {request}")
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
        logger.info(decorated_handler_a.get_output(request))


if __name__ == "__main__":
    main()
