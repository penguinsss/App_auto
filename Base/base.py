import os
import time
from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_ele(self, loc, timeout=5, poll=1.0):
        """定位单个元素"""
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def find_eles(self, loc, timeout=5, poll=1.0):
        """定位多个元素"""
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll=1.0):
        """点击"""
        self.find_ele(loc, timeout, poll).click()

    def send_keys_ele(self, loc, val, timeout=5, poll=1.0):
        """输入文本值"""
        ele = self.find_ele(loc, timeout, poll)
        ele.clear()
        ele.send_keys(val)

    def swipe_page(self, tag=1):
        """
        滑动页面
        :param type: 1：向上滑动 2：向下滑动 3：向左滑动 4：向右滑动
        :return:
        """
        # 等待 防止页面没有跳转进行滑动
        sleep(2)
        size = self.driver.get_window_size()
        width = size.get('width')
        height = size.get('height')
        if tag == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)
        if tag == 2:
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 2000)
        if tag == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)
        if tag == 4:
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 2000)

    def get_toast(self, message):  # ★ 漂亮
        """
        获取手机toast提示消息
        :param message: 拼接获取toast消息xpath文本
        :return:
        """
        mess_xpath = By.XPATH, '//*[contains(@text, {})]'.format(message)
        return self.find_ele(mess_xpath, timeout=3, poll=0.3).text  # ★ 漂亮

    # def screen_png(self):  # ★ 当前appium版本的截图方法 和 uiautomator2冲突
    #     """截图"""
    #     png_name = '.' + os.sep + 'image' + os.sep + '{}.png'.format(int(time.time()))
    #     self.driver.get_screenshot_as_file(png_name)
    #     with open(png_name, 'rb') as f:
    #         allure.attach('截图', f.read(), allure.attach_type.PNG)

    def screen_png(self):  # ★ 替代方案 使用adb进行命令截图
        """截图"""
        png_name = '{}.png'.format(int(time.time()))
        # 截图
        os.system('adb shell screencap -p /sdcard/{}'.format(png_name))
        # 从手机拉取图片到项目
        os.system('adb pull /sdcard/{} ./image'.format(png_name))
        with open('.' + os.sep + 'image' + os.sep + png_name, 'rb') as f:
            allure.attach('截图', f.read(), allure.attach_type.PNG)














