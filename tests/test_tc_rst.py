import pytest

from pages.auth_page import AuthPage
from pages.reg_page import RegPage
from data_test import name_correct, name_dash, name_numb, name_space, name_symbol, name_1_letter, name_2_letter, \
    name_30_letters, name_31_letters, last_name_correct, last_name_symbol, last_name_space, last_name_dash, \
    last_name_numb, last_name_1_letter, last_name_2_letter, last_name_30_letters, last_name_31_letters, \
    password_correct, password_kiril, password_7_digit, password_no_capital, password_8_digit, \
    name_latin, last_name_latin, password_no_symbol_number, conf_pass_uncorrect, user_name_phone, \
    user_name_login, user_name_mail, phone_registration, mail_registration, mail_non_format, phone_non_format

#TC-001, 005, 006, 010 Регистрации по имени удовлетворяющему требованиям
@pytest.mark.parametrize("name", [name_correct, name_2_letter, name_30_letters , name_dash], \
ids=["correct_name", "2_letter_name", "30_letters_name", "name_with_dash"])
def test_registration_by_name_is_suitable(driver, name):
    auth_page = AuthPage(driver)
    reg_page = RegPage(driver)
    auth_page.visit()
    auth_page.link_reg().click()
    reg_page.name().send_keys(name)
    reg_page.last_name().send_keys(last_name_2_letter)
    reg_page.mail_or_phone().send_keys(phone_registration)
    reg_page.password().send_keys(password_correct)
    reg_page.conf_pass().send_keys(password_correct)
    reg_page.btn_reg().click()
    assert reg_page.confirm_phone_mail().is_displayed()

#TC-002 Невозможность регистрации без ввода имени
def test_no_registration_with_empty_name(driver):
    auth_page = AuthPage(driver)
    reg_page = RegPage(driver)
    auth_page.visit()
    auth_page.link_reg().click()
    reg_page.name().send_keys("")
    reg_page.last_name().send_keys(last_name_2_letter)
    reg_page.mail_or_phone().send_keys(phone_registration)
    reg_page.password().send_keys(password_correct)
    reg_page.conf_pass().send_keys(password_correct)
    reg_page.btn_reg().click()
    assert reg_page.requir_on_page().is_displayed()

#TC-003, 004, 007, 008, 009 Невозможность регистрации по имени не удовлетворяющему требованиям, \
# при вводе некорректного имени выводится предупреждение и требование к нему
@pytest.mark.parametrize("name", [name_numb, name_1_letter , name_31_letters, name_space, name_symbol, name_latin], \
 ids=["name_with_number", "1_letter_name", "31_letters_name", "name_with_space", "name_with_specsymbol", \
      "name_with_latin"])
def test_no_registration_by_name_not_suitable(driver, name):
    auth_page = AuthPage(driver)
    reg_page = RegPage(driver)
    auth_page.visit()
    auth_page.link_reg().click()
    reg_page.name().send_keys(name)
    reg_page.last_name().send_keys(last_name_2_letter)
    assert reg_page.requir_on_page().is_displayed()

#TC-011 Невозможность регистрации без ввода фамилии
def test_no_registration_with_empty_last_name(driver):
    auth_page = AuthPage(driver)
    reg_page = RegPage(driver)
    auth_page.visit()
    auth_page.link_reg().click()
    reg_page.name().send_keys(name_correct)
    reg_page.last_name().send_keys("")
    reg_page.mail_or_phone().send_keys(mail_registration)
    reg_page.password().send_keys(password_correct)
    reg_page.conf_pass().send_keys(password_correct)
    reg_page.btn_reg().click()
    assert reg_page.requir_on_page().is_displayed()

#TC-012, 013, 016, 017, 018 Невозможность регистрации по фамилии не удовлетворяющей требованиям, \
# при вводе некорректной фамилии выводится предупреждение и требование к нему
@pytest.mark.parametrize("last_name", \
             [last_name_numb, last_name_1_letter,last_name_31_letters, last_name_space,last_name_symbol, \
              last_name_latin], ids=["last_name_with_number", "1_letter_last_name", "31_letters_last_name", \
                                     "last_name_with_space", "last_name_latin", "last_name_with_specsymbol"])
def test_no_registration_by_name_not_suitable(driver, last_name):
    auth_page = AuthPage(driver)
    reg_page = RegPage(driver)
    auth_page.visit()
    auth_page.link_reg().click()
    reg_page.last_name().send_keys(last_name)
    reg_page.name().send_keys(name_correct)
    assert reg_page.requir_on_page().is_displayed()

#TC-014, 015, 019 Регистрации по фамилии удовлетворяющей требованиям
@pytest.mark.parametrize("last_name", [last_name_2_letter, last_name_30_letters , last_name_dash], \
ids=["2_letter_last_name", "30_letters_last_name", "last_name_with_dash"])
def test_registration_by_last_name_is_suitable(driver, last_name):
    auth_page = AuthPage(driver)
    reg_page = RegPage(driver)
    auth_page.visit()
    auth_page.link_reg().click()
    reg_page.last_name().send_keys(last_name_2_letter)
    reg_page.name().send_keys(name_correct)
    reg_page.mail_or_phone().send_keys(mail_registration)
    reg_page.password().send_keys(password_correct)
    reg_page.conf_pass().send_keys(password_correct)
    reg_page.btn_reg().click()
    assert reg_page.confirm_phone_mail().is_displayed()

#TC-020 Невозможность регистрации без ввода Email или мобильного телефона
def test_no_registration_with_empty_mail(driver):
    auth_page = AuthPage(driver)
    reg_page = RegPage(driver)
    auth_page.visit()
    auth_page.link_reg().click()
    reg_page.name().send_keys(name_correct)
    reg_page.last_name().send_keys(last_name_correct)
    reg_page.mail_or_phone().send_keys("")
    reg_page.password().send_keys(password_correct)
    reg_page.conf_pass().send_keys(password_correct)
    reg_page.btn_reg().click()
    assert reg_page.requir_on_page_mail().is_displayed()

#TC-021, 022 Невозможность регистрации по Email или номеру телефона некорректного формата
@pytest.mark.parametrize("mail_phone", [phone_non_format, mail_non_format], \
ids=["nonformat_phone", "nonformat_mail"])
def test_no_registration_with_empty_mail(driver, mail_phone):
    auth_page = AuthPage(driver)
    reg_page = RegPage(driver)
    auth_page.visit()
    auth_page.link_reg().click()
    reg_page.name().send_keys(name_correct)
    reg_page.last_name().send_keys(last_name_correct)
    reg_page.mail_or_phone().send_keys(mail_phone)
    reg_page.password().send_keys(password_correct)
    reg_page.conf_pass().send_keys(password_correct)
    reg_page.btn_reg().click()
    assert reg_page.requir_on_page_mail().is_displayed()

#TC-023, 025, 026, 027 Невозможность регистрации по паролю не удовлетворяющему требованиям
@pytest.mark.parametrize("password", [password_7_digit, password_no_capital, password_kiril, \
                                      password_no_symbol_number], \
ids=["7_digit_password", "no_capital_password", "kirillica_password", "no_spec_symbol_or_number_password"])
def test_no_registration_by_password_not_suitable(driver, password):
    auth_page = AuthPage(driver)
    reg_page = RegPage(driver)
    auth_page.visit()
    auth_page.link_reg().click()
    reg_page.name().send_keys(name_correct)
    reg_page.last_name().send_keys(last_name_correct)
    reg_page.mail_or_phone().send_keys(mail_registration)
    reg_page.password().send_keys(password)
    reg_page.conf_pass().send_keys(password)
    reg_page.btn_reg().click()
    assert reg_page.requir_on_page_password().is_displayed() or reg_page.requir_on_page_password_short().is_displayed

#TC-024 Регистрация по паролю длиной 8 символов
def test_registration_by_8_digit_password(driver):
    auth_page = AuthPage(driver)
    reg_page = RegPage(driver)
    auth_page.visit()
    auth_page.link_reg().click()
    reg_page.last_name().send_keys(last_name_correct)
    reg_page.name().send_keys(name_correct)
    reg_page.mail_or_phone().send_keys(mail_registration)
    reg_page.password().send_keys(password_8_digit)
    reg_page.conf_pass().send_keys(password_8_digit)
    reg_page.btn_reg().click()
    assert reg_page.confirm_phone_mail().is_displayed()

#TC-028, 029 Невозможность регистрации по не заполненному полю подтверждение пароля или не совпадающему с паролем
@pytest.mark.parametrize("conf_password", ["",conf_pass_uncorrect], \
ids=["no_confirm_password", "uncorrect_confirm_password"])
def test_no_registration_by_empty_or_uncorresct_conf_password(driver, conf_password):
    auth_page = AuthPage(driver)
    reg_page = RegPage(driver)
    auth_page.visit()
    auth_page.link_reg().click()
    reg_page.name().send_keys(name_correct)
    reg_page.last_name().send_keys(last_name_correct)
    reg_page.mail_or_phone().send_keys(mail_registration)
    reg_page.password().send_keys(password_correct)
    reg_page.conf_pass().send_keys(conf_password)
    reg_page.btn_reg().click()
    assert reg_page.requir_on_page_password().is_displayed() or reg_page.requir_on_page_password_short().is_displayed \
    or reg_page.requir_on_page_conf_passw_not_same().is_displayed()


#TC-030 Авторизация по номеру телефона и паролю
def test_correct_authorisation_by_phone(driver):
    auth_page = AuthPage(driver)
    auth_page.visit()
    auth_page.tab_phone().click()
    auth_page.input_username().send_keys(user_name_phone)
    auth_page.input_password().send_keys(password_correct)
    auth_page.voity().click()
    reg_page = RegPage(driver)
    assert reg_page.get_lk().is_displayed()

#TC-031 Авторизация по почте и паролю
def test_correct_authorisation_by_mail(driver):
    auth_page = AuthPage(driver)
    auth_page.visit()
    auth_page.tab_mail().click()
    auth_page.input_username().send_keys(user_name_mail)
    auth_page.input_password().send_keys(password_correct)
    auth_page.voity().click()
    reg_page = RegPage(driver)
    assert reg_page.get_lk().is_displayed()

#TC-032 Авторизация по логину и паролю
def test_correct_authorisation_by_login(driver):
    auth_page = AuthPage(driver)
    auth_page.visit()
    auth_page.tab_login().click()
    auth_page.input_username().send_keys(user_name_login)
    auth_page.input_password().send_keys(password_correct)
    auth_page.voity().click()
    reg_page = RegPage(driver)
    assert reg_page.get_lk().is_displayed()

#TC-034 Авторизация по почте с дефисом и паролю, при выбранном типе аутентификации "Телефон"
def test_auth_by_mail_with_dash_tab_phone(driver):
    auth_page = AuthPage(driver)
    auth_page.visit()
    auth_page.tab_phone().click()
    auth_page.input_username().send_keys(user_name_mail)
    auth_page.input_password().send_keys(password_correct)
    assert auth_page.input_mail()

#TC-035 Авторизация по почте с дефисом и паролю, при выбранном типе аутентификации "Лицевой счет"
def test_mail_with_dash_tab_ls(driver):
    auth_page = AuthPage(driver)
    auth_page.visit()
    auth_page.tab_ls().click()
    auth_page.input_username().send_keys(user_name_mail)
    auth_page.input_password().send_keys(password_correct)
    assert auth_page.input_mail()



