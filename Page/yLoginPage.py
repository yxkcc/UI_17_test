"""
已登录页面操作
"""
import logging

import allure

from Base.base import Base
from .pageElements import PageElements


class YLoginPage(Base):
    def __init__(self):
        super().__init__()
        logging.info("已登录页面")

    @allure.step("点击设置按钮")
    def click_setting_btn(self):
        """点击设置按钮"""
        logging.info("点击设置按钮")
        self.click_ele(PageElements.setting_btn)
