from page.page_index import PageIndex
from page.page_login import PageLogin
from tools.get_driver import GetDriver


class PageIn:
    def __init__(self):
        self.driver = GetDriver.get_driver()

    # 获取pageLogin对象
    def page_get_pageLogin(self):
        return PageLogin(self.driver)

    # 获取pageIndex对象
    def page_get_pageIndex(self):
        return PageIndex(self.driver)
