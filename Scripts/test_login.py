from Base.getDriver import get_android_driver


class TestLogin:
    def setup_class(self):
        self.driver = get_android_driver('com.bjcsxq.chat.carfriend', '.module_main.activity.MainActivity')

    def teardown_class(self):
        self.driver.quit()

    def test_login(self):
        pass