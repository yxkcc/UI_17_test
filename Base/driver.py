"""
百年奥莱包名：com.yunmall.lc
启动名：com.yunmall.ymctoc.ui.activity.MainActivity
"""
from appium import webdriver


class Driver:
    # app driver变量
    __app_driver = None

    @classmethod
    def get_app_driver(cls):
        """声明app driver对象"""
        if cls.__app_driver is None:
            # 如果__app_driver 为空 声明driver对象并返回
            desired_caps = {
                'platformName': 'Android',  # 平台
                'platformVersion': '5.1',  # 平台所属版本
                'deviceName': '192.168.56.101:5555',  # 设备名字 随便写
                'appPackage': 'com.yunmall.lc',  # app包名
                'appActivity': 'com.yunmall.ymctoc.ui.activity.MainActivity',  # app启动名
                # 'noReset': True,
                'automationName': 'Uiautomator2'
            }
            # 声明驱动对象 创建session 打开启动参数中指定的app
            cls.__app_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            return cls.__app_driver
        else:
            # 如果__app_driver不为空 那说明之前已经赋值过 可以继续操作app
            return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        """退出app driver"""
        if cls.__app_driver:
            # 退出
            cls.__app_driver.quit()
            # 手动重置为None
            cls.__app_driver = None
