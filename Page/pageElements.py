from selenium.webdriver.common.by import By


class PageElements:
    """页面元素"""
    """首页"""
    # 关闭更新提示按钮
    close_update = (By.XPATH, "//*[@content-desc='关闭对话框']")
    # “我”导航
    user_navigation = (By.XPATH, "//*[@text='我']")

    """ '我' 未登录页"""
    # “已有账号，去登录提示”
    go_to_login = (By.ID, "com.yunmall.lc:id/textView1")
    # 手机号输入框
    phone_input = (By.ID, "com.yunmall.lc:id/logon_account_textview")
    # 密码输入框
    password_input = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    # 登录按钮
    login_btn = (By.XPATH, "//*[@text='登录']")
    # 退出登录
    close_login = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
    """ '我' 已登录页"""
    # 用户名
    user_name = (By.ID, "com.yunmall.lc:id/tv_user_nikename")
    # 设置按钮
    setting_btn = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
    """设置页面"""
    # 退出按钮
    log_off = (By.XPATH, "//*[@text='退出']")
    # 退出提示确认
    quit_msg_confirm = (By.XPATH, "//*[@text='确认']")
