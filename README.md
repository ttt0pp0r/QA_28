Этот репозиторий содержит автоматизированные тесты, которые проверяют страницы регистрации и авторизации сайта в браузере GoogleChrome: https://b2c.passport.rt.ru/

Для начала работы с тестами необходимо:

1) Скачать репозиторий к себе на компьютер.
2) Извлечь все файлы.
3) Скачать актуальный Selenium WebDriver с сайта: https://chromedriver.chromium.org/downloads (выбрать версию соответствующую версии вашего браузера).
4) Установить все необходимые пакеты, для установки необходимо ввести команду:
```
 pip install -r requirements.txt
```
5) В файле conftest.py в строке 7 указать путь расположения файла chromedriver.exe на вашем компьютере. В пути к файлу "" заменить на "/".
6) Для запуска тестов необходимо ввести команду:
```
 pytest tests\test_tc_rst.py
```
7) Запуск тестов также можно осуществлять в PyCharm, через кнопки запуска тестов.
