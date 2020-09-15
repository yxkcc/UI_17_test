"""
去登录页面
"""
import logging
import allure
from Base.base import Base
from Page.pageElements import PageElements


class GoLoginPage(Base):
    def __init__(self):
        super().__init__()
        logging.info("获取去登录页面")

    @allure.step("点击已有账号去登录")
    def click_go_to_login(self):
        """点击 “去登录” """
        logging.info("点击 “已有账号，去登录” ")
        self.click_ele(PageElements.go_to_login)
