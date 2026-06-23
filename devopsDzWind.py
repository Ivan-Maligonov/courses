import bs4
import time
import winsound
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def play_success():
    winsound.Beep(900, 2000)


def play_beginning():
    duration = 1000
    time.sleep(5)
    winsound.Beep(300, duration)
    time.sleep(1)
    winsound.Beep(300, duration)


def main(url):
    browser = webdriver.Chrome()
    browser.get(url)

    play_beginning()

    result = ("We have received our maximum order capacity "
              "for the day, for this location. Please try again tomorrow.")

    while True:
        now = datetime.now()
        now_string = now.strftime("%Y-%m-%d %H:%M:%S")

        browser.refresh()
        time.sleep(2)

        try:
            wait = WebDriverWait(browser, 30)

            next_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Next']")
                )
            )
            next_button.click()

            print(now_string + " refreshed")

            html = browser.page_source
            soup = bs4.BeautifulSoup(html, "html.parser")

            try:
                element = browser.find_element(
                    By.XPATH,
                    "//*[contains(text(),'We have received our')]"
                )

                print(element.text)

                if result in element.text:
                    print("NO SLOTS :(")
                else:
                    print("OPEN SLOTS!!!!!!!")
                    play_success()

            except Exception:
                print("Сообщение о недоступности не найдено.")
                print("Возможно, появились свободные слоты!")
                play_success()

        except Exception as e:
            print("Ошибка:", e)

        time.sleep(8)


if __name__ == "__main__":
    main("https://www.ikea.com/us/en/")