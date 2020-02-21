from Page.homePage import HomePage
from Page.loginPage import LoginPage
from Page.minePage import MinePage


def get_home_page(driver):
    """首页对象"""
    return HomePage(driver)


def get_mine_page(driver):
    """个人中心"""
    return MinePage(driver)


def get_login_page(driver):
    """登录页面"""
    return LoginPage(driver)


def get_setting_page(driver):
    """设置页面"""
    return LoginPage(driver)