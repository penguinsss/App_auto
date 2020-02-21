from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_ele(self, loc, timeout=5, poll=1):
        """定位单个元素"""
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def find_eles(self, loc, timeout=5, poll=1):
        """定位多个元素"""
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll=1):
        """点击"""
        self.find_ele(loc, timeout, poll).click()

    def send_keys_ele(self, loc, val, timeout=5, poll=1):
        """输入文本值"""
        ele = self.find_ele(loc, timeout, poll)
        ele.clear()
        ele.send_keys(val)

    def get_width_height(self):
        """获取手机的宽高"""
        size = self.driver.get_window_size()
        width = size.get('width')
        height = size.get('height')
        return width, height

    def up_swipe(self):
        """上滑"""
        width, height = self.get_width_height()
        self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)

    def down_swipe(self):
        """下滑"""
        width, height = self.get_width_height()
        self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)