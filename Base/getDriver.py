from appium import webdriver


def get_android_driver(package, activity):
    desired_caps = {'platformName': 'android',
                    'platformVersionName': '5.1',
                    'deviceName': 'sanxing',
                    'appPackage': package,
                    'appActivity': activity,
                    'unicodeKeyboard': True}
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)