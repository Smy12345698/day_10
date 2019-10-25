import sys
import os

sys.path.append(os.getcwd())

import pytest
from tools.read_yaml import read_yaml
from page.page_in import PageIn
from tools.get_driver import GetDriver


def get_data():
    arr = []
    for data in read_yaml("login.yaml").values():
        arr.append((data.get("phone"),
                    data.get("pwd"),
                    data.get("nickname"),
                    data.get("msg"),
                    data.get("toast"),
                    data.get("clickable")))
    return arr


class TestLogin:
    # 初始化
    def setup_class(self):
        self.pageIn = PageIn()
        # 获取PageLogin对象
        self.login = self.pageIn.page_get_pageLogin()
        self.index = self.pageIn.page_get_pageIndex()
        # 点击关闭弹窗
        self.login.page_click_close_alert()
        # 点击我
        self.login.page_click_me()
        # 点击 注册/登录
        self.login.page_click_login_sig()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    # 测试方法
    @pytest.mark.parametrize("phone,pwd,nickname,msg,toast,clickable", get_data())
    def test_login(self, phone, pwd, nickname, msg, toast, clickable):
        # 调用登录业务方法
        self.login.page_login(phone, pwd)
        # 判断是正向还是逆向
        if nickname:
            try:
                # 点击签到确定
                self.login.page_click_sign()
                print("获取的昵称为：", self.index.page_get_nickname())
                # 断言
                assert nickname == self.index.page_get_nickname()
                # 退出登录
                self.index.page_logout()
                # 点击登录/注册
                self.login.page_click_login_sig()
            except Exception as e:
                # 截图
                self.login.base_get_img()
                # 抛出异常
                raise
        elif msg:
            try:
                print("方式1异常提示信息为：",self.login.page_err_info())
                assert msg in self.login.page_err_info()
            except:
                # 截图
                self.login.base_get_img()
                # 抛出异常
                raise
            finally:
                self.login.page_click_err_ok()
        elif toast:
            try:
                # 获取toast消息，并断言
                toast_msg = self.login.page_get_toast(toast)
                print("获取的toast消息为：", toast_msg)
                assert toast in toast_msg

            except:
                # 截图
                self.login.base_get_img()
                # 抛出异常
                raise
        elif clickable:
            result = self.login.page_get_attribute("clickable")
            print("按钮是否可点：", result)
            assert clickable == result
