import logging
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__version__ = '0.1.0'
_LOGGER = logging.getLogger(__name__)


class GoldSensor():
    def __init__(self):
        self._state = None
        self._entries = {}

    def update(self):
        _LOGGER.info("sensor goldprice update info from ")
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
        }
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--auto-open-devtools-for-tabs")
        options.add_argument('headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--window-size=1920,1080");
        driver = webdriver.Chrome(options=options)
        driver.get("https://quote.cngold.org/gjs/swhj_zghj.html")
        goldPricePath = (By.XPATH, '//*[@id="goldTableSum"]/tbody/tr/td[1]/em')
        wait = WebDriverWait(driver, 10)
        goldPrice = wait.until(EC.presence_of_element_located(goldPricePath))
        self._entries["price"] = goldPrice.get_attribute("textContent")
        self._entries["update_time"] = datetime.datetime.now().strftime('%Y-%m-%d')
        return self._entries

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state


    @property
    def extra_state_attributes(self):
        return self._entries





