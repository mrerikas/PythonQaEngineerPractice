import pytest


@pytest.mark.skip
def test_first_program(setup):
    print("Hello World!")


@pytest.mark.xfail
def test_second_program(setup):
    print("Hello again!")


def test_cross_browser(cross_browsers):
    print(cross_browsers[1])
