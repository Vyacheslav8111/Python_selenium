# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.close_browser)
    return fixture


def test_add_group(app):
    app.session.login(username="Admin", password="secret")
    app.group_create(Group(name="s", header="a", footer="f"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="Admin", password="secret")
    app.group_create(Group(name="", header="", footer=""))
    app.session.logout()
