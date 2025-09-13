

# Patron de Diseño con tecnica POM
# Objetivo : Una forma de refactorizar el codigo al instanciar el objeto Page y llamar a asus metodos 

import pytest
from pages.login_page_pom import LoginPage

def test_login_with_pom(page):
    print("Login inicio con POM")
    login= LoginPage(page)
    login.open()
    login.login("standard_user","secret_sauce")
 
    assert page.locator(".inventory_list").is_visible()
    print("Login fin con POM")