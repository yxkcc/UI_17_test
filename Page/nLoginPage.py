"""未登录页面元素操作"""
from Base.base import Base
from .pageElements import PageElements


class NLoginPage(Base):
    def __init__(self):
        super().__init__()

    def click_login_btn(self):
        """点击登录按钮"""
        self.click_ele(PageElements.login_btn)

    def send_phone(self, text):
        """
        输入手机号
        :param text: 用户手机号
        :return:
        """
        self.send_ele(PageElements.phone_input, text)

    def clear_phone(self):
        """清空手机号"""
        self.clear_ele(PageElements.phone_input)

    def clear_password(self):
        """清空密码"""
        self.clear_ele(PageElements.password_input)

    def send_password(self, word):
        """
        输入密码
        :param word: 密码
        :return:
        """
        self.send_ele(PageElements.password_input, word)

    def click_close_login(self):
        """点击关闭登录"""
        self.click_ele(PageElements.close_login)

    def login_operation(self, num, pwd):
        """登录操作"""
        # 输入手机号
        self.send_phone(num)
        # 输入密码
        self.send_password(pwd)
        # 点击登录
        self.click_login_btn()