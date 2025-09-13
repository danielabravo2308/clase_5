
#### Test Case sin refactorizar : Forma Sucia  y de novatos 


import pytest

def test_login_direct(page):
    print("inicio login direct")
    page.goto("https://www.saucedemo.com/")
    page.fill("input[data-test='username']", "standard_user")
    page.fill("input[data-test='password']", "secret_sauce")
    page.click("input[data-test='login-button']")
    assert page.locator(".inventory_list").is_visible()
    print("fin login direct")



    