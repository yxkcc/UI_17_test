"""
正向反向合体
"""

from Base.driver import Driver
from Base.pageFactory import PageFactory
from Base.base import Base
from Base.data import Data
from Page.pageElements import PageElements
import pytest


# 获取数据
def get_data():
    # 存储数据列表
    data_list = list()
    # 读取文件
    data = Data.get_json_data("data01.json")
    for i in data.get("login_data"):
        data_list.append(
            (i.get("phone"),
             i.get("password"),
             i.get("is_true")
             )
        )
    # 不能在循环内返回数据，否则只能得到一条数据
    return data_list


class TestLogin3:
    def setup_class(self):
        """判断登录退出方法"""
        PageFactory.get_home().close_update_btn()

    def teardown_class(self):
        """退出驱动"""
        Driver.quit_app_driver()

    def setup(self):
        # 点击“我”
        PageFactory.get_home().click_user_navigation()
        # 点击“去登录”
        PageFactory.get_go_to_login().click_go_to_login()

    def dc(self):
        """判断登出方法"""
        # 点击设置
        PageFactory.get_y_login().click_setting_btn()
        # 调用登出操作
        PageFactory.get_setting().log_out_operation()
        # # 判断登出是否成功
        if PageFactory.get_home().get_user_navigation_checked() == "true":
            print('\n登出失败')
        else:
            print('\n登出成功')

    @pytest.mark.parametrize("user_phone, password,is_true", get_data())
    def test_login_s(self, user_phone, password, is_true):
        """判断登录成功方法"""
        # 调用登录方法
        PageFactory.get_n_login().login_operation(user_phone, password)
        # 判断登录是否成功
        if is_true:
            try:
                # 查找用户名
                Base().search_ele(PageElements.user_name)
            except:
                print('\n登录失败')
                assert False
            else:
                print('\n登录成功')
                assert True
                self.dc()
        else:
            # 判断登录是否成功
            try:
                # 查找用户名
                Base().search_ele(PageElements.user_name)
            except:
                print('\n登录失败')
                PageFactory.get_n_login().click_close_login()
                assert True
            else:
                print('\n登录成功')
                assert False

# if __name__ == '__main__':
#     pytest.main(["-s", "test_bnal_login5.py"])
