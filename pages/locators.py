from selenium.webdriver.common.by import By

class LoginPageLocators():
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")