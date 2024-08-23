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
    return decorated_handler_a


def test_handler_a(setup_handlers):
    # ทดสอบ ConcreteHandlerA
    handler = ConcreteHandlerA()
    handler.set_next(ConcreteHandlerB())

    with StringIO() as buf, pytest.monkeypatch.context() as mp:
        mp.setattr(sys, 'stdout', buf)
        handler.handle("test")
        output = buf.getvalue()

    assert "Handler A processing request: test" in output


def test_handler_b(setup_handlers):
    # ทดสอบ ConcreteHandlerB
    handler = ConcreteHandlerB()

    with StringIO() as buf, pytest.monkeypatch.context() as mp:
        mp.setattr(sys, 'stdout', buf)
        handler.handle("test")
        output = buf.getvalue()

    assert "Handler B processing request: test" in output


def test_logging_decorator(setup_handlers):
    # ทดสอบ LoggingDecorator
    decorated_handler = setup_handlers

    with StringIO() as buf, pytest.monkeypatch.context() as mp:
        mp.setattr(sys, 'stdout', buf)
        decorated_handler.handle("test")
        output = buf.getvalue()

    assert "Logging request: test" in output


def test_uppercase_decorator(setup_handlers):
    # ทดสอบ UppercaseDecorator
    decorated_handler = setup_handlers

    with StringIO() as buf, pytest.monkeypatch.context() as mp:
        mp.setattr(sys, 'stdout', buf)
        decorated_handler.handle("test")
        output = buf.getvalue()

    assert "Handler A processing request: TEST" in output
    assert "Handler B processing request: TEST" in output

