import pytest


@pytest.fixture()  # @pytest.fixture(scope="class") if setup method run once before methods ("scope="class")
def setup():
    print("\nI will be executing first")
    yield
    print("\nI will be executing last")


@pytest.fixture()
def load_data():
    print("User profile info is being created")
    return ['Erikas', 'Misevicius', 'myemail@email.com']


@pytest.fixture(params=[("chrome", "Erikas", "Misevicius"), ("firefox", "Sigita"), ("msedge", "Karolina")])
def cross_browsers(request):
    return request.param
