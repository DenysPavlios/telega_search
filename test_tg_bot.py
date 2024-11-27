import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import time

load_dotenv()

def test_name():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get('https://t.me/s/raketa_trevoga')

    processed_texts = set()
    keywords = ('борты', 'пуски', 'пуск', 'борт', 'балистика', 'бпла', 'ракет')

    while True:
        driver.refresh()  # Обновляем страницу
        messages = driver.find_elements(By.CSS_SELECTOR, 'div.tgme_widget_message_text.js-message_text')

        if messages:
            last_message = messages[-1]
            chat_text = last_message.text.lower()


            matches = [word for word in keywords if word in chat_text]
            if matches and chat_text not in processed_texts:

                token = os.getenv('TELEGRAM_TOKEN')
                chat_id = '178529845'


                requests.post(
                    f"https://api.telegram.org/bot{token}/sendMessage",
                    json={'chat_id': chat_id, 'text': chat_text}
                )

                processed_texts.add(chat_text)

        time.sleep(5)

test_name()
