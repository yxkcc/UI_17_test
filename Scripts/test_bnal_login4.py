"""
反向登录
"""
from Base.driver import Driver
from Base.pageFactory import PageFactory
from Base.base import Base
from Page.pageElements import PageElements
import pytest


class TestLogin2:
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
            # 点击“去登录”
            PageFactory.get_go_to_login().click_go_to_login()

    @pytest.mark.parametrize("user_phone, password", [("1386286716", "5201314yxk"), ("13862867165", "5201314yxk"),
                                                      ("13862867164", "5201314yx")])
    def test_login(self, user_phone, password):
        """判断登录成功方法"""
        # 输入手机号
        PageFactory.get_n_login().send_phone(user_phone)
        # 输入密码
        PageFactory.get_n_login().send_password(password)
        # 点击登录
        PageFactory.get_n_login().click_login_btn()
        # 判断登录是否成功
        try:
            # 查找用户名
            Base().search_ele(PageElements.user_name)
        except:
            print('\n登录失败')
            assert True
        else:
            print('\n登录成功')
            assert False


if __name__ == '__main__':
    pytest.main(["-s", "test_bnal_login4.py"])
