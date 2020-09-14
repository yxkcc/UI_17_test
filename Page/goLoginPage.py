"""
去登录页面
"""
from Base.base import Base
from Page.pageElements import PageElements


class GoLoginPage(Base):
    def __init__(self):
        super().__init__()

    def click_go_to_login(self):
        """点击 “去登录” """
        self.click_ele(PageElements.go_to_login)
