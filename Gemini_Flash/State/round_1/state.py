#Gemini_Flash coding test in the same file

from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def on_enter(self, context):
        pass

    @abstractmethod
    def on_exit(self, context):
        pass

    @abstractmethod
    def handle_event(self, context, event):
        pass

class Context:
    def __init__(self):
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        if self._state:
            self._state.on_exit(self)
        self._state = new_state
        self._state.on_enter(self)

    def handle_event(self, event):
        self._state.handle_event(self, event)

class OffState(State):
    def on_enter(self, context):
        print("Turning off")

    def on_exit(self, context):
        print("Turning on")

    def handle_event(self, context, event):
        if event == "turn_on":
            context.state = OnState()

class OnState(State):
    def on_enter(self, context):
        print("Turning on")

    def on_exit(self, context):
        print("Turning off")

    def handle_event(self, context, event):
        if event == "turn_off":
            context.state = OffState()

class TestContext:
    def __init__(self):
        self.state = None
        self.events = []

    def set_state(self, state):
        self.state = state

    def record_event(self, event):
        self.events.append(event)

    def handle_event(self, event):
        self.state.handle_event(self, event)

class TestState(State):
    def on_enter(self, context):
        context.record_event("enter_" + self.__class__.__name__)

    def on_exit(self, context):
        context.record_event("exit_" + self.__class__.__name__)

    def handle_event(self, context, event):
        context.record_event(event)
        if event == "transition":
            context.set_state(context.state.next_state)

class State1(TestState):
    next_state = State2

class State2(TestState):
    next_state = State3

class State3(TestState):
    next_state = State1

def test_state_machine_on_off():
    context = Context()
    context.state = OffState()
    assert context.state == OffState()

    context.handle_event("turn_on")
    assert context.state == OnState()

    context.handle_event("turn_off")
    assert context.state == OffState()

def test_state_machine_transition():
    context = TestContext()
    context.set_state(State1())
    context.handle_event("transition")
    assert context.events == ["enter_State1", "transition", "exit_State1", "enter_State2"]

    context.handle_event("transition")
    assert context.events == ["enter_State1", "transition", "exit_State1", "enter_State2", "transition", "exit_State2", "enter_State3"]

    context.handle_event("transition")
    assert context.events == ["enter_State1", "transition", "exit_State1", "enter_State2", "transition", "exit_State2", "enter_State3", "transition", "exit_State3", "enter_State1"]
