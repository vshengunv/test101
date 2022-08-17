import re
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import getpass

from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import os

# 定义一个元素高亮的方法
def HighLightElement(driver,element):
    #使用js将传入的页面元素对象的背景颜色和边框颜色分辨设置为 绿色 和 红色
    driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,"background:green ;border:2px solid red;")


class TestPay():
    #定义一个打开web网站的方法
    def WebStart(self):
        firefoxstart = webdriver.Chrome()

    def Opentestweb(url='https://test.yingzhongshare.com/index-frontend/index.html#/login'):
        # xmiles_Account = input("请输入账号：")
        # xmiles_Password = input("请输入密码：")
        # prdid = input("请输入需要打款的prdid:")
        brower = webdriver.Chrome()

        # 使用WebDriver的事件监听类
        driver = EventFiringWebDriver(brower, EventListeners())
        driver.get(url)
        time.sleep(2)

        # #对协程函数TestListening赋值(监听方法应该有误这里暂时不做)
        # result = await TestPay().TestListening()

        # 定位元素输入账号
        driver.find_element(By.NAME, 'username').send_keys("fanqing")
        # 定位元素输入密码
        driver.find_element(By.NAME, 'password').send_keys("ciTlY+Ch0HF=k*Hi%6A")
        # js定位登录按钮
        js_login = 'document.querySelector("button.el-button.login-btn.el-button--primary").click()'
        driver.execute_script(js_login)

        time.sleep(2)
        # 定位元素点击发行中台
        test_element_DistributionCenter = driver.find_element(By.XPATH,
                                                              "//*[@id='app']/div/div[2]/div/div/div[12]/div[2]/p[1]")
        # 元素高亮
        HighLightElement(driver, test_element_DistributionCenter)
        time.sleep(1)
        # 进入发行中台系统
        test_element_DistributionCenter.click()
        # # 打印当前窗口尺寸,并设置尺寸大小
        # print(driver.get_window_size())
        # driver.set_window_size(1500,1060)
        # driver.maximize_window()
        time.sleep(5)
        # 进入frame框架
        driver.switch_to.frame(frame_reference='XMIframe')
        test_element_InternationalVersion = driver.find_element(By.XPATH, "//div[text()='国际版']")
        driver.execute_script('arguments[0].click()', test_element_InternationalVersion)
        # 定位元素开发者下拉框
        test_element_Developers = driver.find_element(By.XPATH,
                                                      "//li//div//span[@class='ant-menu-title-content' and text()='开发者']")
        # 元素高亮
        HighLightElement(driver, test_element_Developers)
        time.sleep(1)
        # 进入开发者下拉框
        test_element_Developers.click()
        time.sleep(2)
        # 进入提现审核二部
        """
        使用WebDriver点击界面上Button元素时，如果当前Button元素被界面上其他元素遮住了，
        或没出现在界面中（比如Button在页面底部，但是屏幕只能显示页面上半部分），
        使用默认的WebElement.Click()可能会触发不了Click事件。
        execute_script方法可以调用原生JavaScript的api
        需加上browser.execute_script(‘arguments[0].click()’, webElement);
        """
        # #直接选择下拉框中的元素
        # driver.find_element(By.XPATH, "//a[text()='提现审核_二部']").click()
        test_element_CashWithdrawalAudit = driver.find_element(By.XPATH, "//li[8]//span//a[text()='提现审核_二部']")
        HighLightElement(driver, test_element_CashWithdrawalAudit)
        # 调用js的api点击被遮挡的按钮
        driver.execute_script('arguments[0].click()', test_element_CashWithdrawalAudit)
        # 退出frame框架
        # driver.switch_to.default_content()
        # 输入产品prdid
        time.sleep(3)
        driver.find_element(By.XPATH, "//div//span//input[@id='search_form_prdId']").send_keys("777889")
        driver.find_element(By.XPATH, "//div//span//input[@id='search_form_prdId']").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element(By.ID,"search_form_transferStatus").click()
        driver.find_element(By.ID, "search_form_transferStatus").send_keys(Keys.ENTER)
        # driver.find_element(By.ID, 'search_form_prdId').submit()
        # time.sleep(1)
        # 查询该产品
        driver.find_element(By.XPATH, "//span[text()='查 询']").click()
        time.sleep(1)
        # #批量走人工审核通过,选择每页的条目数量
        # driver.find_element(By.XPATH,"//sapn[text()='20 条/页']").click()
        # test_element_Entry=driver.find_element(By.XPATH,"//span[text()='100 条/页']")
        # driver.execute_script('arguments[0].click()',test_element_Entry)
        # time.sleep(2)
        try:
            for i in range(10):
                # 批量操作id全选
                driver.find_element(By.XPATH, "//tr//th//div//label//span//input[@class='ant-checkbox-input']").click()
                time.sleep(2)
                # 批量操作按钮点击
                driver.find_element(By.XPATH,
                                    "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/button/span[1]").click()
                # 点击审核通过
                test_element_Through = driver.find_element(By.XPATH,
                                                           "//ul//li//span[@class='ant-dropdown-menu-title-content']/div")
                HighLightElement(driver, test_element_Through)
                time.sleep(1)
                driver.execute_script('arguments[0].click()', test_element_Through)
                # 操作确认
                # driver.find_element(By.XPATH,"//div[@class='ant-popover-buttons]/button[1]/span")
                test_element_Confirm = driver.find_element(By.XPATH,
                                                           "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div/div[2]/div/div[2]/button[2]/span")
                driver.execute_script("arguments[0].click()", test_element_Confirm)
                time.sleep(2)
                driver.find_element(By.XPATH, "//span[text()='查 询']").click()
                time.sleep(1)
                # 打印是第几遍打款
                print("第{}遍".format(i + 1))
                if i == 9:
                    print("结束了，已经打款了将近200条哦！")
        except BaseException as msg:
            print("已经没有可以操作的了" + msg)
        driver.quit()

#定义一个WebDriver的事件监听的类
class EventListeners(AbstractEventListener):
    """
    selenium事件监听：搜索 ’selenium.webdriver.support.events‘
    调用监听类的时候会把监听点击的函数一起调用了，所以这里先注释掉
    """
    # #定义一个函数监听点击前的元素
    # def before_click(self, element, driver):
    #     print("before_click %s" % element)
    # #定义一个函数监听点击后元素
    # def after_click(self, element, driver):
    #     print("after_click %s" % element)

    #定义一个函数监听WebDriver报错时浏览器的开关状态
    def on_exception(self, exception, driver):
        print("WebDriver异常")
        TestListening = 1
        while TestListening == 1:
            object_existed = False
            if driver is not None:
                try:
                    driver.execute_script('javascript:void(0);')
                    object_existed = True
                    print("浏览器开着")
                    return 1
                except:
                    try:
                        driver.quit()
                    finally:
                        pass
            if not object_existed:
                print("浏览器已关闭")
                TestListening += 1
                ...
            time.sleep(1)
        return 1







if __name__ == '__main__':
    # xmiles_accout = 'fanqing'
    # xmiles_password = 'ciTlY+Ch0HF=k*Hi%6Au' 'ciTlY+Ch0HF=k*Hi%6A'
    TestPay.Opentestweb()
