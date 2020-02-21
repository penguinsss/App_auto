from Base.base import Base
from Page.pageElements import PageElements


class LoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, phone, pwd):
        # 输入账号
        self.send_keys_ele(PageElements.login_phone_id, phone)
        # 输入密码
        self.send_keys_ele(PageElements.login_pwd_id, pwd)
        # 点击登录
        self.click_ele(PageElements.login_btn_id)

    def login_acc(self):
        """登录成功确认"""
        self.click_ele(PageElements.login_neg_btn_id)

    def login_back(self):
        """登录页面返回"""
        self.click_ele(PageElements.login_back_id)
