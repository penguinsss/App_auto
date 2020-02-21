from appium import webdriver


def get_android_driver(package, activity):
    """
    安卓手机驱动对象
    :param package: 包名
    :param activity: 启动名
    :return: 驱动对象
    """
    desired_caps = {'platformName': 'android',
                    'platformVersionName': '5.1',
                    'deviceName': 'sanxing',
                    'appPackage': package,
                    'appActivity': activity,
                    'unicodeKeyboard': True,
                    'automationName': 'Uiautomator2'}   # ★ toast消息，只支持原生toast消息
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)