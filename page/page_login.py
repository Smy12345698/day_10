import page
from base.base import Base


class PageLogin(Base):
    # 关闭弹窗
    def page_click_close_alert(self):
        self.base_click(page.login_close_alert)

    # 点击我
    def page_click_me(self):
        self.base_click(page.login_me)

    # 点击登录/注册
    def page_click_login_sig(self):
        self.base_click(page.login_sig)

    # 输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.login_phone, phone)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录
    def page_click_login(self):
        self.base_click(page.login_btn)

    # 点击签到确定
    def page_click_sign(self):
        self.base_click(page.login_sign)

    # 获取异常提示信息
    def page_err_info(self):
        return self.base_get_text(page.login_err_info)

    # 获取toast消息
    def page_get_toast(self, msg):
        return self.base_get_toast(msg)

    # 点击异常提示框确定按钮
    def page_click_err_ok(self):
        self.base_click(page.login_confirm)

    def page_get_attribute(self,att):
        return self.base_get_attribute(page.login_btn,att)

    # 组合业务方法
    def page_login(self, phone, pwd):
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login()
