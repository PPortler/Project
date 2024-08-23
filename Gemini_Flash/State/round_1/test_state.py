from state_pattern import (
    OffState,
    OnState,
    Context,
    TestContext,
    State1,
    State2,
    State3,
    test_state_machine_on_off,
    test_state_machine_transition,
)

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
