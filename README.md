#### Скрипты автотестов

Папка testing_url - решение через парсинг страницы.

Папка testing_url_selenium - решение через использование WebDriver.

Testing_url.side - решение через использование SeleniumIDE.

#### Что необходиомо для запуска скриптов

Скрипты testing_url.py и testing_url_selenium.py написаны на python3.

Для установки пакетов python - pip v10.0.1

В testing_url_selenium.py используется FireFox. Тестировалось в версии FireFox 60.0.2 (64-бит), Windows 7 SP1.

Для запуска тестов использовался:
* интерпретатор python v3.6.5
* geckodriver v0.21.0
* seleniumIDE v3.1.0 (в Chrome 67.0.3396.87)

Дополнительные требования указаны в файлах requirements.txt в папках со скриптами.

#### Запуск

Установить интерпретатор python

Установить пакеты python:
* запустить командную строку
* поочередно выполнить команды:

  pip install bs4

  pip install lxml

  pip install requests

  pip install selenium

Скачать и добавить в переменные среды путь до geckodriver

Установить в Chrome плагин SeleniumIDE

##### Запуск скриптов testing_url.py / testing_url_selenium.py:
* в командной строке набрать и выполнить:

  python script_name.py

##### Запуск Testing_url.side:
* запустить файл в SeleniumIDE
