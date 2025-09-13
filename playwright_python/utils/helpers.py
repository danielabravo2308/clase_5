

def assert_visible(page,selector,msg="Elemento no visible"):
    assert page.locator(selector).is_visible(),msg