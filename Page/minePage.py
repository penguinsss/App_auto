from Base.base import Base
from Page.pageElements import PageElements


class MinePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def go_to_login(self):
        """点击个人中心登录/注册按钮"""
        self.click_ele(PageElements.mine_login_reg_xpath)   # ★ PageElements 类似于By

    def get_username(self):
        """获取登录用户"""
        return self.find_ele(PageElements.mine_login_username_id).text

    def go_to_setting(self):
        """点击设置"""
        self.click_ele(PageElements.mine_setting_id)