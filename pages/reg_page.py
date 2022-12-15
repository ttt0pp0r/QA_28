from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegPage():
    def __init__(self, driver):
        self.driver = driver

    def get_lk(self):
        return self.driver.find_element(By.ID, "lk-btn")


    def name(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(((By.XPATH, "//input[@name='firstName']"))))
        return self.driver.find_element(By.XPATH, "//input[@name='firstName']")

    def last_name(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(((By.XPATH, "//input[@name='lastName']"))))
        return self.driver.find_element(By.XPATH, "//input[@name='lastName']")

    def mail_or_phone(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(((By.ID, "address"))))
        return self.driver.find_element(By.ID, "address")

    def password(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(((By.ID, "password"))))
        return self.driver.find_element(By.ID, "password")

    def conf_pass(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(((By.ID, "password-confirm"))))
        return self.driver.find_element(By.ID, "password-confirm")

    def btn_reg(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(((By.XPATH, "//button[@name='register']"))))
        return self.driver.find_element(By.XPATH, "//button[@name='register']")

    def requir_on_page(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(), 'Необходимо')]")

    def requir_on_page_mail(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'Введите телефон')]")

    def requir_on_page_password_short(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'Длина пароля')]") \

    def requir_on_page_password(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'Пароль')]")

    def requir_on_page_conf_passw_not_same(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'Пароли')]")
    def confirm_phone_mail(self):
        return self.driver.find_element(By.XPATH, "//h1[contains(text(),'Подтверждение')]")

    # Подтверждение E-mail
    # //h1[contains(text(),'Подтверждение email')]

    # Подтверждение телефона
    # //h1[contains(text(),'Подтверждение телефона')]