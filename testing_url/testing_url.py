import requests
from bs4 import BeautifulSoup

url_page = 'http://blog.csssr.ru/qa-engineer/'
true_link = 'http://monosnap.com/'


def get_html(url):                  # Открываем сайт, получаем html страницу
    r = requests.get(url)
    return r.text


def get_link(html):                 # Парсим страницу с искомым url
    soup = BeautifulSoup(html, 'lxml')
    link = soup.find('div', class_='info-errors').find('a').get('href')
    return link


def main():                         # Итоговая проверка
    html_page = get_html(url_page)
    test_link = get_link(html_page)
    try:
        assert test_link == true_link
    except AssertionError:
        print("Найден баг!")


if __name__ == '__main__':
    main()
