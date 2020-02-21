from Base.base import Base
from Page.pageElements import PageElements


class SettingPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def logout(self, tag=1):  # ★ 等于1确认退出，等于2取消退出
        """点击退出当前帐号"""
        self.click_ele(PageElements.set_logout_btn_id)
        if tag == 1:
            self.click_ele(PageElements.set_logout_ok_btn)
            # 退出后向下滑
            self.swipe_page(2)        # ★ 合并的漂亮！
        if tag == 2:
            self.click_ele(PageElements.set_logout_dis_xpath)

