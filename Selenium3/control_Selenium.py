import re
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


#定义一个打开浏览器的类
class WebOpen():
    def WebStart(self):
        driver = webdriver.Firefox()


driver = webdriver.Firefox()
#定义一个监测浏览器关闭的类
def testcase():
    driver.get("https://www.baidu.com")
    TestListening = 1
    while TestListening == 1 :
        object_existed = False
        if driver is not None:
            try:
                driver.execute_script('javascript:void(0);')
                object_existed = True
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






def Openbaidu(url='https://www.baidu.com'):
    driver.get(url)

    # 通过参数数字设置浏览器的高宽
    driver.set_window_size(480, 800)
    time.sleep(3)

    driver.maximize_window()  # 浏览器窗口最大化
    driver.find_element(By.CSS_SELECTOR, '.s_ipt').send_keys("Selenium")
    driver.find_element(By.CSS_SELECTOR, '#su').click()
    # driver.find_element(By.CSS_SELECTOR, '#su').submit()            #通过submit方法模拟 Enter 键操作来提交表单
    # 返回（后退）到百度首页
    print("返回前的url:", driver.current_url)  # 通过 dirver.current_url() 方法获取当前网页的url
    time.sleep(2)
    driver.back()
    # 前进到新闻页
    print("返回后的url:", driver.current_url)
    time.sleep(2)
    driver.forward()
    # driver.refresh()  # 通过 dirver.refresh() 刷新页面
    time.sleep(5)
    driver.quit()


def Open126(url="https://mail.126.com/"):
    # 登录126邮箱
    driver.get(url)
    time.sleep(10)
    try:
        # driver.switch_to.frame()      进入frame嵌套页面内查找。--注意 driver.find_elenment 只能在一个页面查找元素
        driver.switch_to.frame(driver.find_element(By.NAME, ""))
        # driver.switch_to.default_content()            退出当前嵌套，即回到当前页面的被嵌套页面
    except BaseException as msg:
        print("frame没有定位到",msg)
    try:
        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "email").send_keys("vlinzhijiangv")
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys('12345')
        driver.find_element(By.ID, "dologin").click()
    except BaseException:
        print("账号、密码或者登录按钮没有定位到")
    # driver.quit()

def WebelementFunction(url='https://www.baidu.com'):                #Webelement接口常用的方法
    driver.get(url)
    print("输入框尺寸为：",driver.find_element(By.ID,"kw").size)                     #获得输入框的尺寸
    print("备案号为：",driver.find_element(By.ID,"bottom_layer").text)              #获取百度底部页面的备案信息
    print("元素的属性值为：",driver.find_element(By.ID,"kw").get_attribute("type"))  #获取元素的属性值，可以是id、name、type或其他属性
    print("元素是否可见：",driver.find_element(By.ID,"kw").is_displayed())           #返回元素的结果是否可见，结果为 True 或 False
    print("driver.find_element(By.CSS_SELECTOR, '#su').submit()   通过submit()方法模拟Enter按键提交表单")

def Yunpan360(url="http://yunpan.360.cn"):
    driver.get(url)
    driver.find_element(By.XPATH,"//a[text()='360帐号登录']").click()
    driver.find_element(By.NAME,"userName").send_keys("7aowe187sf@crossmailjet.com")
    driver.find_element(By.NAME,"password").send_keys("Lsyx12345.com")
    # driver.find_element(By.NAME, "password").submit()                           #通过 submit() 提交表单的形式直接绕过元素的隐藏属性而登录

#   — —  通过js来点击hidden的元素或是display：none的元素
    js = 'document.querySelector("input.quc-button-submit").click()'
    driver.execute_script(js)
    time.sleep(20)
#   —   —通过定位续费关闭按钮(这里还没做完，因为不会) —   —
"""
   close_element = "//*[name()='svg']/*[name()='use']/*[name()='symbol']"
    svgelement = driver.find_element(By.XPATH,close_element)
    close_action = ActionChains(svgelement)
    close_action.context_click(svgelement).perform()
    # driver.find_element(By.XPATH,"//*[@id='/html/body/div[8]/div[2]/div[1]/svg']//*[@name()='svg']").click()
    # driver.find_element(By.XPATH,"//svg[@class='close-icon' and @clssa='icon-svg']")
    print("1111111")
"""


def ControlMouse(url='https://www.baidu.com'):
    from selenium.webdriver.common.action_chains import ActionChains            #导入鼠标事件模块，引入ActionChains类
    driver.get(url)
    Lsyx = "7aowe187sf@crossmailjet.com"





if __name__ == '__main__':
    # WebOpen.WebStart()
    # Open126()
    # Openbaidu()
    # WebelementFunction()
    # Yunpan360()
    testcase()
    print("Over")
