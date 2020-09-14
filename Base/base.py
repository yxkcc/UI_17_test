import logging

from selenium.webdriver.support.wait import WebDriverWait
from Base.driver import Driver
import time


class Base:

    def __init__(self):
        self.driver = Driver.get_app_driver()

    def search_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: (类型,属性值)
        :param timeout: 超时时间
        :param poll_frequency: 搜索间隔
        :return: 定位对象
        """
        logging.info("操作元素:{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: (类型,属性值)
        :param timeout: 超时时间
        :param poll_frequency: 搜索间隔
        :return: 定位对象列表
        """
        logging.info("操作一组元素:{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        点击元素
        :param loc: (类型,属性值)
        :param timeout: 超时时间
        :param poll_frequency: 搜索间隔
        :return:
        """
        logging.info("执行点击操作")
        self.search_ele(loc, timeout, poll_frequency).click()

    def send_ele(self, loc, text, timeout=5, poll_frequency=1.0):
        """
        输入框 输入文本
        :param loc: (类型,属性值)
        :param text: 输入的文本内容
        :param timeout: 超时时间
        :param poll_frequency: 搜索间隔
        :return:
        """
        logging.info("执行输入动作，输入内容为:{}".format(text))
        # 定位
        ele = self.search_ele(loc, timeout, poll_frequency)
        # 清空
        ele.clear()
        # 输入
        ele.send_keys(text)

    def clear_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        清空操作
        :param loc:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        logging.info("执行清空操作")
        self.search_ele(loc, timeout, poll_frequency).clear()

    # 封装滑动方法
    def swipe_screen(self, tag=1, duration=1500):
        """
        滑动屏幕方法
        :param duration: 滑动时间(ms)
        :param tag:1:向上 2:向下 3:向左 4:向右
        :return:
        """
        logging.info("执行滑动操作{},滑动时间为{}".format(tag,duration))
        # 获取屏幕分辨率
        size = self.driver.get_window_size()
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")
        # 等待
        time.sleep(2)
        # 滑动
        if tag == 1:
            # 垂直向上：起点：宽 * 50 %，高 * 80 % -> 宽 * 50 %，高 * 20 %
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, duration)
        if tag == 2:
            # 垂直向下 起点：宽*50%，高*20% -> 宽*50%，高*80%
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, duration)
        if tag == 3:
            # 水平向左 起点：宽*80%，高*50% -> 宽*20%，高50%
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, duration)
        if tag == 4:
            # 水平向右 起点：宽*20%，高*50% -> 宽*80%，高50%
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, duration)
