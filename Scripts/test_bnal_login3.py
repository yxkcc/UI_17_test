"""
正向登录
"""

from Base.driver import Driver
from Base.pageFactory import PageFactory
from Base.base import Base
from Page.pageElements import PageElements
import pytest


class TestLogin1:
    def teardown_class(self):
        """退出驱动"""
        Driver.quit_app_driver()

    def setup_class(self):
        """判断登录退出方法"""
        try:
            # 查找“更新提示”
            Base().search_ele(PageElements.close_update)
        except:
            pass
        else:
            # 点击“x”
            PageFactory.get_home().click_close_update()
        finally:
            # 点击“我”
            PageFactory.get_home().click_user_navigation()

    def dc(self):
        """判断登出方法"""
        # 点击设置
        PageFactory.get_y_login().click_setting_btn()
        # 调用登出操作
        PageFactory.get_setting().log_out_operation()
        # 点击“我”
        PageFactory.get_home().click_user_navigation()
        # 判断登出是否成功
        try:
            # 查找“已有账号，去登录”
            Base().search_ele(PageElements.go_to_login)
        except:
            print('\n登出失败')
        else:
            print('\n登出成功')

    @pytest.mark.parametrize("user_phone, password", [("13862867164", "5201314yxk"), (" 13862867164", "5201314yxk"),
                                                      ("13862867164 ", "5201314yxk")])
    def test_login(self, user_phone, password):
        """判断登录成功方法"""
        # 点击“去登录”
        PageFactory.get_go_to_login().click_go_to_login()
        # 调用登录方法
        PageFactory.get_n_login().login_operation(user_phone, password)
        # 判断登录是否成功
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


if __name__ == '__main__':
    pytest.main(["-s", "test_bnal_login3.py"])
