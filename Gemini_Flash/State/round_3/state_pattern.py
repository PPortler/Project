class State:
    """
    Base class for all states.
    """

    def handle(self, context):
        """
        Handle the context in the current state.
        """
        raise NotImplementedError()


class StateA(State):
    """
    State A implementation.
    """

    def handle(self, context):
        print("State A: Handling context...")
        context.set_state(StateB())


class StateB(State):
    """
    State B implementation.
    """

    def handle(self, context):
        print("State B: Handling context...")
        context.set_state(StateA())


class Context:
    """
    Context class to manage the state.
    """

    def __init__(self, state: State):
        self._state = state

    def set_state(self, state: State):
        self._state = state

    def handle(self):
        self._state.handle(self)
