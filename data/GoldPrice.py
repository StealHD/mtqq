import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bean.WebSeed import WebSeed


class GoldPrice():
    def __init__(self):
        self._entries = {}


    def update(self, url, driver):
        driver.get(url)
        goldPricePath = (By.XPATH, '//*[@id="goldTableSum"]/tbody/tr/td[1]/em')
        wait = WebDriverWait(driver, 10)
        goldPrice = wait.until(EC.presence_of_element_located(goldPricePath))
        self._entries["price"] = goldPrice.get_attribute("textContent")
        self._entries["update_time"] = datetime.datetime.now().strftime('%Y-%m-%d')
        return self._entries

    def extra_state_attributes(self):
        return self._entries

# driver = WebSeed().driver()
# web = GoldPrice()
# wedData=web.get_data(driver=driver, url="https://quote.cngold.org/gjs/swhj_zghj.html")
# print(web.extra_state_attributes)







