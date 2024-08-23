from state_pattern import StateA, StateB, Context

def test_state_a():
    context = Context(StateA())
    context.handle()
    assert isinstance(context._state, StateB)

def test_state_b():
    context = Context(StateB())
    context.handle()
    assert isinstance(context._state, StateA)
