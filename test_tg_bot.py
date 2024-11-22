import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()
from selenium.webdriver.chrome.options import Options
import time

def test_name():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get('https://t.me/s/openqwertya')

    processed_texts = set()

    while True:
        driver.refresh()
        bitcoin_today = driver.find_elements(
            By.CSS_SELECTOR, 'div.tgme_widget_message_text.js-message_text')

        if bitcoin_today:
            element_last = bitcoin_today[-1]
            bitcoin_text = element_last.text.lower()
            print('--------')

            if ('борты', 'пуски', 'пуск', 'борт','балистика' in bitcoin_text) and bitcoin_text not in processed_texts:
                # Получаем токен из переменной окружения
                token = os.getenv('TELEGRAM_TOKEN')
                chat_id = '178529845'

                requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                              json={'chat_id': chat_id, 'text': bitcoin_text})

                processed_texts.add(bitcoin_text)

        time.sleep(5)

test_name()

# sss