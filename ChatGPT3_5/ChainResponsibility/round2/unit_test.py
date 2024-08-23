import pytest
from io import StringIO
import sys

# นำเข้า classes จากไฟล์หลัก
from code import Handler, ConcreteHandlerA, ConcreteHandlerB, LoggingDecorator, UppercaseDecorator


@pytest.fixture
def setup_handlers():
    # สร้าง handlers และ decorators
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_a.set_next(handler_b)

    decorated_handler_a = LoggingDecorator(UppercaseDecorator(handler_a))
    return decorated_handler_a, handler_a, handler_b


def test_concrete_handler_a(setup_handlers):
    # ทดสอบ ConcreteHandlerA
    _, handler_a, _ = setup_handlers

    # Capture output
    with StringIO() as buf, pytest.monkeypatch.context() as mp:
        mp.setattr(sys, 'stdout', buf)
        handler_a.handle("test")
        output = buf.getvalue()

    assert "Handler A processing request: test" in output


def test_concrete_handler_b(setup_handlers):
    # ทดสอบ ConcreteHandlerB
    _, _, handler_b = setup_handlers

    # Capture output
    with StringIO() as buf, pytest.monkeypatch.context() as mp:
        mp.setattr(sys, 'stdout', buf)
        handler_b.handle("test")
        output = buf.getvalue()

    assert "Handler B processing request: test" in output


def test_logging_decorator(setup_handlers):
    # ทดสอบ LoggingDecorator
    decorated_handler, _, _ = setup_handlers

    # Capture output
    with StringIO() as buf, pytest.monkeypatch.context() as mp:
        mp.setattr(sys, 'stdout', buf)
        decorated_handler.handle("test")
        output = buf.getvalue()

    assert "Logging request: test" in output


def test_uppercase_decorator(setup_handlers):
    # ทดสอบ UppercaseDecorator
    decorated_handler, _, _ = setup_handlers

    # Capture output
    with StringIO() as buf, pytest.monkeypatch.context() as mp:
        mp.setattr(sys, 'stdout', buf)
        decorated_handler.handle("test")
        output = buf.getvalue()

    assert "Handler A processing request: TEST" in output
    assert "Handler B processing request: TEST" in output


def test_chain_with_decorators(setup_handlers):
    # ทดสอบ Chain of Responsibility กับ Decorators
    decorated_handler, _, _ = setup_handlers

    # Capture output
    with StringIO() as buf, pytest.monkeypatch.context() as mp:
        mp.setattr(sys, 'stdout', buf)
        decorated_handler.handle("test")
        output = buf.getvalue()

    assert "Logging request: TEST" in output
    assert "Handler A processing request: TEST" in output
    assert "Handler B processing request: TEST" in output

