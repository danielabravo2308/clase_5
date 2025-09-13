
# Patron de Diseño con tecnica DRY

import pytest
from pages.login_page_dry import LoginPageDry
from utils.helpers import assert_visible


def test_login_dry(page):
    login = LoginPageDry(page)
    login.open()
    login.login("standard_user","secret_sauce")
    assert_visible(page,".inventory_list","No se encontro la lista de productos ")
