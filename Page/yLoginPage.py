"""
已登录页面操作
"""
from Base.base import Base
from .pageElements import PageElements


class YLoginPage(Base):
    def __init__(self):
        super().__init__()

    def click_setting_btn(self):
        """点击设置按钮"""
        self.click_ele(PageElements.setting_btn)

