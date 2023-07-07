import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(username="Admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.close_browser()
    request.addfinalizer(fin)
    return fixture
