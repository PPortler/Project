from abc import ABC, abstractmethod

class State(ABC):
    """Abstract base class for all states."""

    @abstractmethod
    def handle_input(self, context, input):
        """Handles input and transitions to other states."""
        pass

class OnState(State):
    """State when the device is on."""

    def handle_input(self, context, input):
        if input == "OFF":
            context.transition_to(OffState())
            print("Device turned off.")
        elif input == "VOLUME_UP":
            context.volume += 1
            print(f"Volume increased to {context.volume}")
        elif input == "VOLUME_DOWN":
            context.volume -= 1
            print(f"Volume decreased to {context.volume}")
        else:
            print("Invalid input.")

class OffState(State):
    """State when the device is off."""

    def handle_input(self, context, input):
        if input == "ON":
            context.transition_to(OnState())
            print("Device turned on.")
        else:
            print("Invalid input. Device is off.")

class Context:
    """Context that holds the current state and manages transitions."""

    def __init__(self):
        self.state = OffState()
        self.volume = 0

    def transition_to(self, state):
        """Transitions to a new state."""
        self.state = state

    def handle_input(self, input):
        """Handles input by delegating to the current state."""
        self.state.handle_input(self, input)

if __name__ == "__main__":
    device = Context()
    while True:
        input_str = input("Enter input (ON, OFF, VOLUME_UP, VOLUME_DOWN): ")
        device.handle_input(input_str)
