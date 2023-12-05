from bean.WebSeed import WebSeed
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ExchangeRate():
    def __init__(self):
        self._entries = {}


    def update(self, url, driver):
        dictList = ['币种', '汇率']
        rateDict = {}
        try:
            # 打开网页
            driver.get(url)
            # 使用显式等待等待c-wiz元素可见
            wait = WebDriverWait(driver, 10)
            c_wiz_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'bF2Mne')))
            # 这时c-wiz元素应该可见，可以继续进行其他操作
            # 例如，你可以获取c-wiz元素的文本内容
            c_wiz_text = c_wiz_element.text
            data = str(c_wiz_text).split("\n")
            result = [data[i:i + 4] for i in range(0, len(data), 4)]
            for i in dictList:
                for lis in result:
                    rateDict[lis[2]] = lis[1]
        finally:
            pass

        self._entries = rateDict
        self._entries["update_time"] = datetime.datetime.now().strftime('%Y-%m-%d')
        return self._entries


    @property
    def extra_state_attributes(self):
        return self._entries

# driver = WebSeed().driver()
# web = GoldPrice()
# url = "https://www.google.com/finance/quote/AUD-CNY"
# wedData=web.get_data(driver=driver, url=url)
# print(web.extra_state_attributes)






