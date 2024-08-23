import pytest
from chain_of_responsibility import (
    ChainOfResponsibility,
    ConcreteHandler1,
    ConcreteHandler2,
    DefaultHandler,
)


class MockHandler(Handler):
    """Mock handler for testing."""

    def __init__(self):
        self.handled = False

    def handle_request(self, request):
        self.handled = True
        return False  # Always pass the request to the next handler


@pytest.mark.parametrize(
    "request, expected_handler",
    [("A", ConcreteHandler1), ("B", ConcreteHandler2), ("C", DefaultHandler)],
)
def test_handle_request(request, expected_handler, monkeypatch):
    """Test that the correct handler is called for each request."""
    chain = ChainOfResponsibility()
    chain.add_handler(ConcreteHandler1())
    chain.add_handler(ConcreteHandler2())

    # Use mock handlers to track which handler is called
    mock_handler1 = MockHandler()
    mock_handler2 = MockHandler()
    mock_default_handler = MockHandler()

    monkeypatch.setattr(
        "chain_of_responsibility.ConcreteHandler1.handle_request",
        mock_handler1.handle_request,
    )
    monkeypatch.setattr(
        "chain_of_responsibility.ConcreteHandler2.handle_request",
        mock_handler2.handle_request,
    )
    monkeypatch.setattr(
        "chain_of_responsibility.DefaultHandler.handle_request",
        mock_default_handler.handle_request,
    )

    chain.handle_request(request)

    # Assert that the correct handler was called
    assert expected_handler is not None
    if expected_handler == ConcreteHandler1:
        assert mock_handler1.handled is True
        assert mock_handler2.handled is False
        assert mock_default_handler.handled is False
    elif expected_handler == ConcreteHandler2:
        assert mock_handler1.handled is True
        assert mock_handler2.handled is True
        assert mock_default_handler.handled is False
    elif expected_handler == DefaultHandler:
        assert mock_handler1.handled is True
        assert mock_handler2.handled is True
        assert mock_default_handler.handled is True


def test_add_handler():
    """Test that add_handler() adds a handler to the chain."""
    chain = ChainOfResponsibility()
    chain.add_handler(ConcreteHandler1())
    assert len(chain._handlers) == 1
    assert isinstance(chain._handlers[0], ConcreteHandler1)
