from selenium.common.exceptions import TimeoutException

from Base.base import Base
from Page.pageElements import PageElements


class HomePage(Base):
    """首页"""

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_later_update(self):    
        # 点击稍后更新
        try:
            # 老版本提示更新 执行点击操作
            self.click_ele(PageElements.home_later_update_id)
        except TimeoutException:
            # 新版本app没有提示框
            print('当前没有找到元素')

    def click_mine(self):
        # 点击我的
        self.click_ele(PageElements.home_mine_id)
