from selenium import webdriver
from time import sleep

url_page = "http://blog.csssr.ru/qa-engineer/"
true_title = "Monosnap - программа для создания скриншотов"


def main():
    browser = webdriver.Firefox()
    browser.get(url_page)
    sleep(2)
    tab_link = browser.find_element_by_link_text("НАХОДИТЬ НЕСОВЕРШЕНСТВА")
    tab_link.click()
    link_from_tab = browser.find_element_by_link_text("Софт для быстрого создания скриншотов")
    link_from_tab.click()
    sleep(2)
    current_window = browser.current_window_handle
    new_window = [i for i in browser.window_handles if i != current_window]
    browser.switch_to.window(new_window[0])
    new_title = browser.page_source
    try:
        assert "Monosnap - программа для создания скриншотов" in new_title
    except AssertionError:
        print("Найден баг!")
    sleep(2)
    browser.quit()


if __name__ == '__main__':
    main()
