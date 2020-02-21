import os
import sys

# ★ 添加自定义模块到python搜索路径
import time

sys.path.append(os.getcwd())  # 这行代码必须在导入其他模块之前导入
import pytest
from Base.getData import GetData
from Base.getDriver import get_android_driver
from Base.page import Page


def data(yml_name):
    lis = []
    data_list = GetData().get_yml_data(yml_name)
    for i in data_list:
        lis.append((i.get('phone'),
                    i.get('password'),
                    i.get('toast_mess'),
                    i.get('exp_data')))
    return lis


class TestLogin:
    def setup_class(self):
        self.driver = get_android_driver('com.bjcsxq.chat.carfriend', '.module_main.activity.MainActivity')
        self.page = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope='class', autouse=True)
    def goto_mine(self):
        """进入个人中心"""
        # 首页点击稍后更新
        self.page.get_home_page().click_later_update()
        # 首页点击我的
        self.page.get_home_page().click_mine()

    @pytest.fixture(autouse=True)
    def goto_login(self):
        """进入登录页面"""
        # 我的页面点击登录/注册按钮
        self.page.get_mine_page().go_to_login()

    @pytest.mark.parametrize('phone, password, toast_mess, exp_data', data('login.yml'))
    def test_login(self, phone, password, toast_mess, exp_data):
        """
        测试方法
        :param phone:手机号
        :param password: 密码
        :param toast_mess: 提示消息
        :param exp_data: 预期结果
        :return:
        """
        # 登录页面输入账号
        self.page.get_login_page().login(phone, password)
        if toast_mess is None:
            """正向测试用例"""
            # 登录页面点击登录确认
            self.page.get_login_page().login_acc()
            # 个人中心获取用户名
            username = self.page.get_mine_page().get_username()
            try:
                assert username == exp_data
            except AssertionError:
                self.page.get_login_page().screen_png()
                raise
            finally:
                # 个人中心 设置
                self.page.get_mine_page().go_to_setting()
                # 设置页面 退出
                self.page.get_setting_page().logout()
        else:
            """逆向测试用例"""
            toast = self.page.get_login_page().get_toast('错误')
            try:
                # 断言
                assert toast == exp_data
            except AssertionError:  # ★ 只有断言错误才会捕获
                # 截图
                self.page.get_login_page().screen_png()
                # 抛出断言异常
                raise
            finally:
                # 登录页面点击返回
                self.page.get_login_page().login_back()
