
def test_first_program(setup):
    msg = "Hello"
    assert msg == "Hello", f"Test failed, because {msg} not equal to 'Hi'"


def test_second_program(setup):
    a = 2
    b = 3
    assert a + b == 5, f"Test failed, a + b = {a + b}"
