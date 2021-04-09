import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo_1(self):
        print("I'm test method")

    def test_fixture_demo_2(self):
        print("I'm test method")

    def test_fixture_demo_3(self):
        print("I'm test method")

    def test_first_program(self):
        msg = "Hello"
        assert msg == "Hello", f"Test failed, because {msg} not equal to 'Hi'"

    def test_second_program(self):
        a = 2
        b = 3
        assert a + b == 5, f"Test failed, a + b = {a + b}"
