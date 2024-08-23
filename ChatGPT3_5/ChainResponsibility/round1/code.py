from abc import ABC, abstractmethod


# Base Handler class for Chain of Responsibility
class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        pass


# Concrete Handlers
class ConcreteHandlerA(Handler):
    def handle(self, request):
        print(f"Handler A processing request: {request}")
        if self._next_handler:
            self._next_handler.handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        print(f"Handler B processing request: {request}")
        if self._next_handler:
            self._next_handler.handle(request)


# Base Handler Decorator
class HandlerDecorator(Handler):
    def __init__(self, handler):
        super().__init__()
        self._handler = handler

    def set_next(self, handler):
        self._handler.set_next(handler)
        return handler

    def handle(self, request):
        self._handler.handle(request)


# Concrete Decorators
class LoggingDecorator(HandlerDecorator):
    def handle(self, request):
        print(f"Logging request: {request}")
        super().handle(request)


class UppercaseDecorator(HandlerDecorator):
    def handle(self, request):
        request = request.upper()
        super().handle(request)


# Main function to demonstrate functionality
def main():
    # Create handlers
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()

    # Set up chain of responsibility
    handler_a.set_next(handler_b)

    # Decorate handlers
    decorated_handler_a = LoggingDecorator(UppercaseDecorator(handler_a))

    # Process requests
    requests = ["request 1", "request 2"]
    for request in requests:
        decorated_handler_a.handle(request)


if __name__ == "__main__":
    main()
