from selenium import webdriver


class WebSeed():
    def __init__(self):
        self._state = None
        self._entries = {}
        self._options = webdriver.ChromeOptions()
        self._options.add_argument("--disable-blink-features=AutomationControlled")
        self._options.add_argument("--auto-open-devtools-for-tabs")
        self._options.add_argument('headless')
        self._options.add_argument('--no-sandbox')
        self._options.add_argument('--disable-dev-shm-usage')
        self._options.add_argument("--window-size=1920,1080");
        # self._options.add_argument(
        #     "--disable-blink-features=AutomationControlled "
        #     "--auto-open-devtools-for-tabs --headless --no-sandbox --disable-dev-shm-usage --window-size=1920,1080"
        # )
        self._header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
        }

    def driver(self, options=None, header=None):
        if options is None:
            options = self._options
        if header is None:
            header = self._header
        driver = webdriver.Chrome(options=options)
        # driver.get(url)
        # self.get_data(driver)
        return driver

    def get_data(self, url, driver):
        # driver.get(url)
        # goldPricePath = (By.XPATH, '//*[@id="goldTableSum"]/tbody/tr/td[1]/em')
        # wait = WebDriverWait(driver, 10)
        # goldPrice = wait.until(EC.presence_of_element_located(goldPricePath))
        # self._entries["price"] = goldPrice.get_attribute("textContent")
        # self._entries["update_time"] = datetime.datetime.now().strftime('%Y-%m-%d')
        return

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._entries

# resource = GoldSensor().update()
# print(resource)
