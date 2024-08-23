from state_pattern import OnState, OffState, Context

def test_device_on():
    device = Context()
    device.handle_input("ON")
    assert device.state == OnState()

def test_device_off():
    device = Context()
    device.handle_input("ON")
    device.handle_input("OFF")
    assert device.state == OffState()

def test_volume_up():
    device = Context()
    device.handle_input("ON")
    device.handle_input("VOLUME_UP")
    assert device.volume == 1

def test_volume_down():
    device = Context()
    device.handle_input("ON")
    device.handle_input("VOLUME_UP")
    device.handle_input("VOLUME_DOWN")
    assert device.volume == 0

def test_invalid_input_on():
    device = Context()
    device.handle_input("INVALID")
    assert device.state == OffState()

def test_invalid_input_off():
    device = Context()
    device.handle_input("ON")
    device.handle_input("OFF")
    device.handle_input("INVALID")
    assert device.state == OffState()

def test_invalid_input_volume():
    device = Context()
    device.handle_input("ON")
    device.handle_input("INVALID")
    assert device.volume == 0
