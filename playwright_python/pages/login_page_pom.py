# Patron de Diseño con tecnica POM
# Cada metodo realiza una tarea especifica


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.user = "input[data-test='username']"
        self.pwd = "input[data-test='password']"
        self.btn = "input[data-test='login-button']"

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self,username,password):
        self.page.fill(self.user, username)
        self.page.fill(self.pwd, password)
        self.page.click(self.btn)

    