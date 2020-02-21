from selenium.webdriver.common.by import By


class PageElements:
    """项目页面元素定位"""

    """首页"""
    # 稍后更新
    home_later_update_id = By.ID, 'com.bjcsxq.chat.carfriend:id/bt_no'
    # 我的按钮
    home_mine_id = By.ID, 'com.bjcsxq.chat.carfriend:id/mine_layout'

    """个人中心"""
    # 登录/注册  用户名昵称   把id留给用户名
    mine_login_reg_xpath = By.XPATH, '//*[contails(@text, "登录/注册")]'
    # 用户名
    mine_login_username_id = By.ID, 'com.bjcsxq.chat.carfriend:id/mine_username_tv'
    # 设置
    mine_setting_id = By.ID, 'com.bjcsxq.chat.carfriend:id/setting_icon'

    """登录"""
    # 账号
    login_phone_id = By.ID, 'com.bjcsxq.chat.carfriend:id/login_phone_et'
    # 密码
    login_pwd_id = By.ID, 'com.bjcsxq.chat.carfriend:id/login_pwd_et'
    # 登录
    login_btn_id = By.ID, 'com.bjcsxq.chat.carfriend:id/login_btn'
    # 登录页面返回按钮
    login_back_id = By.ID, 'com.bjcsxq.chat.carfriend:id/title_back'
    # 登录成功后的确定
    login_neg_btn_id = By.ID, 'com.bjcsxq.chat.carfriend:id/btn_neg'

    """设置"""
    # 退出当前账号
    set_logout_btn_id = By.ID, 'com.bjcsxq.chat.carfriend:id/set_logout_tv'
    # 确定
    set_logout_ok_btn = By.ID, 'com.bjcsxq.chat.carfriend:id/bt_ok'
    # 取消
    set_logout_dis_xpath = By.XPATH, '//*[contails(@text, "取消")]'

