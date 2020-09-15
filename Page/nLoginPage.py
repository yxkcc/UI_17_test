"""未登录页面元素操作"""
import allure

from Base.base import Base
from .pageElements import PageElements
import logging


class NLoginPage(Base):
    def __init__(self):
        super().__init__()
        logging.info("登录页面")

    @allure.step("点击登录按钮")
    def click_login_btn(self):
        """点击登录按钮"""
        logging.info("点击登录按钮")
        self.click_ele(PageElements.login_btn)

    @allure.step("输入手机号")
    def send_phone(self, text):
        """
        输入手机号
        :param text: 用户手机号
        :return:
        """
        logging.info("输入手机号:{}".format(text))
        self.send_ele(PageElements.phone_input, text)

    def clear_phone(self):
        """清空手机号"""
        self.clear_ele(PageElements.phone_input)

    def clear_password(self):
        """清空密码"""
        self.clear_ele(PageElements.password_input)

    @allure.step("输入密码")
    def send_password(self, word):
        """
        输入密码
        :param word: 密码
        :return:
        """
        logging.info("输入密码:{}".format(word))
        self.send_ele(PageElements.password_input, word)

    @allure.step("点击关闭登录")
    def click_close_login(self):
        """点击关闭登录"""
        logging.info("点击关闭登录")
        self.click_ele(PageElements.close_login)

    def login_operation(self, num, pwd):
        """登录操作"""
        logging.info("登录操作")
        # 输入手机号
        self.send_phone(num)
        # 输入密码
        self.send_password(pwd)
        # 点击登录
        self.click_login_btn()
