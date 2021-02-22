from ..framework.base_page import BasePage
from ..framework.logger import Logger



logger = Logger(logger="BasePage").getlog()
class login_page(BasePage):
    def __init__(self):
        super().__init__()
    #登录页手机号输入框
    def Login_phone_input(self):
        element=self.find_element( "xpath => //*[@calss='u1']/a[7]")
        self.type(element,'18520434246')
        return logger.info("登录页手机号输入框")
    #密码输入
    def Login_password_input(self):
        element = self.find_element("xpath => //*[@id='u1']/a[7]")
        self.type(element, '8888888ywd')
        return logger.info("登录页手机号输入框")#需要点击前输出后买你处理
    #点击登录
    def Login_click(self):
        element = self.find_element("xpath => //*[@id='u1']/a[7]")
        self.click(element)
        return logger.info("登录页手机号输入框")