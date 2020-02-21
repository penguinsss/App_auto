from Page.homePage import HomePage
from Page.loginPage import LoginPage
from Page.minePage import MinePage


class Page:
    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        """首页对象"""
        return HomePage(self.driver)

    def get_mine_page(self):
        """个人中心"""
        return MinePage(self.driver)

    def get_login_page(self):
        """登录页面"""
        return LoginPage(self.driver)

    def get_setting_page(self):
        """设置页面"""
        return LoginPage(self.driver)
