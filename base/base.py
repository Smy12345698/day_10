import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化
    def __init__(self, driver):
        """
        :param driver: 驱动对象
        """
        # 获取对象
        self.driver = driver

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):
        """

        :param loc: 元组由元素的定位方式及值组成  如：By.ID，"..."
        :param timeout: 默认查找元素时间30秒
        :param poll: 查找元素频率 0.5秒找一次
        :return: 找到的元素
        """
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击
    def base_click(self, loc):
        """
        :param loc: 元素的定位信息，格式为元组
        """
        self.base_find(loc).click()

    # 输入
    def base_input(self, loc, value):
        """
        :param loc: 元素的定位信息，格式为元组
        :param value: 要输入的内容
        """
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本
    def base_get_text(self, loc):
        """
        :param loc: 元素的定位信息，格式为元组
        :return: 返回元素的文本信息
        """
        # 一定要返回
        return self.base_find(loc).text

    # 获取toast提示消息
    def base_get_toast(self, msg):
        """

        :param msg: toast消息框包含的文本
        :return: 获取的toast消息
        """
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(msg)
        return self.base_find(loc, timeout=3, poll=0.2).text

    # 获取截图
    def base_get_img(self):
        self.driver.get_screenshot_as_file("./image/err.png")
        # 调用将图片写入报告
        self.base_write_img()

    # 将图片写入allure报告
    def base_write_img(self):
        with open("./image/err.png", "rb")as f:
            allure.attach("失败原因：", f.read(), allure.attach_type.PNG)

    #获取属性值方法
    def base_get_attribute(self,loc,att):
        return self.base_find(loc).get_attribute(att)
