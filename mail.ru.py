import time
from datetime import datetime
import winsound

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def play_success():
    winsound.Beep(900, 500)


def play_beginning():
    winsound.Beep(300, 500)
    time.sleep(1)
    winsound.Beep(300, 500)


def main():

    options = webdriver.ChromeOptions()

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    browser.maximize_window()

    try:
        browser.get("https://mail.ru")

        play_beginning()

        while True:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            browser.refresh()

            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            print("----------------------------------------")
            print("Время:", now)
            print("Заголовок:", browser.title)
            print("URL:", browser.current_url)

            if "mail.ru" in browser.current_url.lower():
                print("✓ Mail.ru успешно открыт")
                play_success()
            else:
                print("✗ Сайт не открыт")

            time.sleep(10)

    except KeyboardInterrupt:
        print("Программа остановлена пользователем.")

    finally:
        browser.quit()


if __name__ == "__main__":
    main()