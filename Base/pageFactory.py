from Page.settingPage import SettingPage
from Page.homePage import HomePage
from Page.nLoginPage import NLoginPage
from Page.yLoginPage import YLoginPage
from Page.goLoginPage import GoLoginPage


class PageFactory:
    @classmethod
    def get_home(cls):
        """返回首页对象"""
        return HomePage()

    @classmethod
    def get_setting(cls):
        """返回设置页面对象"""
        return SettingPage()

    @classmethod
    def get_n_login(cls):
        """返回未登录页面对象"""
        return NLoginPage()

    @classmethod
    def get_y_login(cls):
        """返回已登录页面对象"""
        return YLoginPage()

    @classmethod
    def get_go_to_login(cls):
        """返回去登录页面对象"""
        return GoLoginPage()
