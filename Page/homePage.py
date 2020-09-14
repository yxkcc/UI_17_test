"""
首页元素操作
"""
from Base.base import Base
from Page.pageElements import PageElements


class HomePage(Base):
    """首页元素操作"""

    def __init__(self):
        super().__init__()

    def click_close_update(self):
        """点击 'x' """
        self.click_ele(PageElements.close_update)

    def click_user_navigation(self):
        """点击 '我' 导航"""
        self.click_ele(PageElements.user_navigation)

    def get_user_navigation_checked(self):
        """获取我 checked属性值"""
        return self.search_ele(PageElements.user_navigation).get_attribute("checked")

    def close_update_btn(self):
        """关闭更新提示"""
        try:
            # 查找“更新提示”
            Base().search_ele(PageElements.close_update)
        except:
            pass
        else:
            # 点击“x”
            self.click_close_update()
