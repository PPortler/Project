import pytest
from io import StringIO
import logging
from contextlib import redirect_stdout
from code import VendingMachine, WaitingForMoneyState, HasMoneyState, DispensingItemState, OutOfStockState

# Set up logging configuration for tests
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger()

@pytest.fixture
def setup_vending_machine():
    """Fixture to set up a Vending Machine with 1 item."""
    vending_machine = VendingMachine(item_count=1)
    return vending_machine

def capture_output(func, *args, **kwargs):
    """Helper function to capture output from print statements."""
    f = StringIO()
    with redirect_stdout(f):
        func(*args, **kwargs)
    return f.getvalue()

def test_initial_state(setup_vending_machine):
    """Test that the vending machine initializes with the correct state."""
    vending_machine = setup_vending_machine
    assert isinstance(vending_machine.state, WaitingForMoneyState)

def test_insert_money_transition(setup_vending_machine):
    """Test inserting money transitions to HasMoneyState."""
    vending_machine = setup_vending_machine
    vending_machine.insert_money()
    assert isinstance(vending_machine.state, HasMoneyState)

def test_turn_crank_dispense_item(setup_vending_machine):
    """Test turning the crank in HasMoneyState and dispensing an item."""
    vending_machine = setup_vending_machine
    vending_machine.insert_money()
    vending_machine.turn_crank()
    assert isinstance(vending_machine.state, WaitingForMoneyState)
    assert vending_machine.item_count == 0

def test_dispense_item_out_of_stock():
    """Test vending machine behavior when out of stock."""
    vending_machine = VendingMachine(item_count=0)
    vending_machine.insert_money()
    output = capture_output(vending_machine.turn_crank)
    assert "Out of stock. Can't turn the crank." in output
    assert "Out of stock. No item to dispense." in output
    assert isinstance(vending_machine.state, OutOfStockState)

def test_insert_money_eject_when_out_of_stock():
    """Test inserting money and ejection when out of stock."""
    vending_machine = VendingMachine(item_count=0)
    vending_machine.insert_money()
    output = capture_output(vending_machine.eject_money)
    assert "Out of stock. Money returned." in output
    assert isinstance(vending_machine.state, WaitingForMoneyState)

def test_turn_crank_when_item_out_of_stock():
    """Test turning the crank when out of stock."""
    vending_machine = VendingMachine(item_count=0)
    output = capture_output(vending_machine.turn_crank)
    assert "Out of stock. Can't turn the crank." in output
    assert "Out of stock. No item to dispense." in output
    assert isinstance(vending_machine.state, OutOfStockState)

def test_multiple_transitions(setup_vending_machine):
    """Test multiple transitions and ensure correct behavior."""
    vending_machine = setup_vending_machine
    vending_machine.insert_money()
    vending_machine.turn_crank()
    assert vending_machine.item_count == 0
    vending_machine.insert_money()
    output = capture_output(vending_machine.turn_crank)
    assert "Out of stock. Can't turn the crank." in output
    assert "Out of stock. No item to dispense." in output
    assert isinstance(vending_machine.state, OutOfStockState)

if __name__ == "__main__":
    pytest.main()
