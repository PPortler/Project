import pytest
import logging
from io import StringIO
from code import ConcreteHandlerA, ConcreteHandlerB, LoggingDecorator, UppercaseDecorator

# Set up logging configuration for tests
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger()


@pytest.fixture
def setup_handlers():
    # Create handlers and decorators
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_a.set_next(handler_b)

    decorated_handler_a = LoggingDecorator(UppercaseDecorator(handler_a))
    return decorated_handler_a, handler_a, handler_b


def test_concrete_handler_a(setup_handlers):
    """Test ConcreteHandlerA"""
    _, handler_a, _ = setup_handlers
    output = handler_a.get_output("test request")
    assert "Handler A processing request: test request" in output


def test_concrete_handler_b(setup_handlers):
    """Test ConcreteHandlerB"""
    _, _, handler_b = setup_handlers
    output = handler_b.get_output("test request")
    assert "Handler B processing request: test request" in output


def test_logging_decorator(setup_handlers):
    """Test LoggingDecorator"""
    decorated_handler, _, _ = setup_handlers
    output = decorated_handler.get_output("test request")
    assert "Logging request: test request" in output


def test_uppercase_decorator(setup_handlers):
    """Test UppercaseDecorator"""
    decorated_handler, _, _ = setup_handlers
    output = decorated_handler.get_output("test request")
    assert "Handler A processing request: TEST REQUEST" in output
    assert "Handler B processing request: TEST REQUEST" in output


def test_chain_with_decorators(setup_handlers):
    """Test Chain of Responsibility with Decorators"""
    decorated_handler, _, _ = setup_handlers
    output = decorated_handler.get_output("test request")
    assert "Logging request: TEST REQUEST" in output
    assert "Handler A processing request: TEST REQUEST" in output
    assert "Handler B processing request: TEST REQUEST" in output
