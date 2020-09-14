"""
设置页面元素操作
"""
import logging

from Base.base import Base
from .pageElements import PageElements


class SettingPage(Base):

    def __init__(self):
        super().__init__()
        logging.info("设置页面")

    def click_log_off(self):
        """点击退出"""
        logging.info("点击退出")
        self.click_ele(PageElements.log_off)

    def click_quit_msg_confirm(self):
        """点击退出提示确认"""
        logging.info("点击退出提示确认")
        self.click_ele(PageElements.quit_msg_confirm)

    def swipe_screen_down(self):
        """垂直向上滑动"""
        logging.info("垂直向上滑动")
        self.swipe_screen()

    def log_out_operation(self):
        """登出操作"""
        logging.info("登出操作")
        # 滑动页面
        self.swipe_screen_down()
        # 点击退出
        self.click_log_off()
        # 点击确认
        self.click_quit_msg_confirm()
