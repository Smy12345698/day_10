import page
from base.base import Base


class PageIndex(Base):
    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 点击设置
    def page_click_setting(self):
        self.base_click(page.login_setting)

    # 点击 退出登录
    def page_click_logout(self):
        self.base_click(page.login_logout)

    # 确认退出
    def page_click_logout_ok(self):
        self.base_click(page.login_logout_ok)

    # 组合退出业务
    def page_logout(self):
        self.page_click_setting()
        self.page_click_logout()
        self.page_click_logout_ok()
