from config import url
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage():
    def __init__(self, driver):
        self.driver=driver

    def visit(self):
        self.driver.get(url)

    def get_auth(self):
        return self.driver.find_element(By.XPATH, "//h1[contains(text(),'Авторизация')]")

    def input_username(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(((By.ID, 'username'))))
        return self.driver.find_element(By.ID, 'username')

    def input_password(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
        return self.driver.find_element(By.ID, "password")

    def voity(self):
        return self.driver.find_element(By.ID, "kc-login")

    def tab_phone(self):
        return self.driver.find_element(By.ID, "t-btn-tab-phone")

    def tab_mail(self):
        return self.driver.find_element(By.ID, "t-btn-tab-mail")

    def tab_login(self):
        return self.driver.find_element(By.ID, "t-btn-tab-login")

    def tab_ls(self):
        return self.driver.find_element(By.ID, "t-btn-tab-ls")

    def link_reg(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-register")))
        return self.driver.find_element(By.ID, "kc-register")

    def input_mail(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'dainisvasiljev@gmail.com')]")


