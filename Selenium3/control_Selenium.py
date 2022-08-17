import re
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
# 导入元素等待库
from selenium.webdriver.support.ui import WebDriverWait
# 导入expected_conditions类所提供的预期条件判断
from selenium.webdriver.support import expected_conditions as EC




#定义一个打开浏览器的类
class WebOpen():
    def WebStart(self):
        driver = webdriver.Firefox()



driver = webdriver.Firefox()
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
        driver.find_element(By.NAME, "email").send_keys("linzhi")
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys('12345')
        driver.find_element(By.ID, "dologin").click()
    except BaseException:
        print("账号、密码或者登录按钮没有定位到")
    time.sleep(10)
    print(driver.title)
    #退出嵌套
    driver.switch_to.default_content()
    #获取登录的用户名
    try:
        user_126 = driver.find_element(By.CSS_SELECTOR, "#spnUid").text
        print(user_126)
    except:
        print("126")





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
    """
    鼠标事件：
    from selenium.webdriver import ActionChains     导入提供鼠标操作的ActionChains类。
    ActionChains(driver)        调用ActionChains()类，将浏览器驱动driver作为参数传入。
    context_click(right_click)      context_click()方法用于模拟鼠标右键操作，在调用时需要指定元素定位。
    perform()               执行所有ActionChains中存储的行为，可以理解成是对整个操作的提交动作。

    键盘事件：
#输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

send_keys(Keys.BACK_SPACE)　　　　　 删除键（BackSpace）
send_keys(Keys.SPACE)　　　　　　　　空格键(Space)
send_keys(Keys.TAB)　　　　　　　　　制表键(Tab)
send_keys(Keys.ESCAPE)　　　　　　　 回退键（Esc）
send_keys(Keys.ENTER)　　　　　　　　回车键（Enter）
send_keys(Keys.CONTROL,'a')　　　　　全选（Ctrl+A）
send_keys(Keys.CONTROL,'c')　　　　　复制（Ctrl+C）
send_keys(Keys.CONTROL,'x')　　　　　剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v')　　　　　粘贴（Ctrl+V）
send_keys(Keys.F1)　　　　　　　　　 键盘F1
send_keys(Keys.F12)　　　　　　　　　键盘F12
    """
    from selenium.webdriver.common.action_chains import ActionChains            #导入鼠标事件模块，引入ActionChains类
    driver.get(url)
    #存储定位到的元素
    right_click = driver.find_element(By.CSS_SELECTOR,"#su")
    textimput = driver.find_element(By.CSS_SELECTOR,"#kw")
    takephoto = driver.find_element(By.CSS_SELECTOR,".soutu-btn")
    #鼠标悬停
    ActionChains(driver).move_to_element(takephoto).perform()
    time.sleep(2)
    #键入搜索的内容
    textimput.send_keys("远离毒品，珍爱生命")
    #鼠标左键双击该元素
    ActionChains(driver).double_click(right_click).perform()
    time.sleep(1)
    #鼠标右键点击该元素
    ActionChains(driver).context_click(right_click).perform()
    #鼠标拖动  drag_and_drop(source,target) source:鼠标拖动的源元素 target:鼠标释放的目标元素
    # ActionChains(driver).drag_and_drop(right_click,takephoto).perform()
    Lsyx = "7aowe187sf@crossmailjet.com"

#定义一个元素等待的类
class WaitUtil(object):
    """
    WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
    driver ：浏览器驱动。
    timeout ：最长超时时间，默认以秒为单位。
    poll_frequency ：检测的间隔（步长）时间，默认为0.5S。
    ignored_exceptions ：超时后的异常信息，默认情况下抛NoSuchElementException异常。

    WebDriverWait()一般由until()或until_not()方法配合使用，下面是until()和until_not()方法的说明。
        ·　until(method, message=‘ ’)
    调用该方法提供的驱动程序作为一个参数，直到返回值为True。
        ·　until_not(method, message=’ ’)
    调用该方法提供的驱动程序作为一个参数，直到返回值为False。
    """
    def __init__(self, driver):
        self.locationTypeDict = {
            "xpath": By.XPATH,
            "id": By.ID,
            "name": By.NAME,
            "css_selector": By.CSS_SELECTOR,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT
        }
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def visibility_element_located(self, locationType, locatorExpression, *args):
        """
        显示等待页面元素的出现
        :param locationType:
        :param locatorExpression:
        :param arg:
        :return:
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((self.locationTypeDict[locationType.lower()], locatorExpression)))
            return element
        except Exception as e:
            raise e
    def presence_of_element_located(self,locationType,locatorExpression,*args):
        """
        显示等待页面元素出现再DOM中，但是并不一定可见，存在则返回该页面元素对象
        :param location:
        :param locatorExpression:
        :param args:
        :return:
        """
        try:
            element = self.wait.until(
                EC.presence_of_element_located((self.locationTypeDict[locationType.lower()],locatorExpression))
            )
        except Exception as e:
            raise e
"""
expected_conditions类提供的预期条件判断的方法:
title_is	                        判断当前页面的标题是否等于预期
title_contains	                    判断当前页面的标题是否包含预期字符串
presence_of_element_located	        判断元素是否被加在DOM树里，并不代表该元素一定可见
visibility_of_element_located   	判断元素是否可见（可见代表元素非隐藏，并且元素的宽和高都不等于0）
visibility_of	                    与上一个方法作用相同，只是上一个方法参数为定位，该方法接收的参数为定位后的元素
presence_of_all_elements_located	判断是否至少有一个元素存在于DOM树中。例如，在个页面中有n个元素的class为“wp”，那么只要有一个存在就返回True
text_to_be_present_in_element   	判断某个元素中的text是否包含了预期的字符串
text_to_be_present_in_element_value	判断某个元素的value属性是否包含了预期的字符串
frame_to_be_available_and_switch_to_it	判断该表单是否可以切换进去，如果可以，返回True并且switch进去，否则返回False
invisibility_of_element_located 	判断某个元素是否不存在于DOM树或不可见
element_to_be_clickable         	判断元素是否可见并且是可以点击的
staleness_of                    	等到一个元素从DOM树中移除
element_to_be_selected          	判断某个元素是否被选中，一般用在下拉列表
element_selection_state_to_be   	判断某个元素的选中状态是否符合预期
element_located_selection_state_to_be	与上一个方法作用相同，只是上一个方法参数为定位后的元素，该方法接收的参数为定位
alert_is_present                	判断页面上是否存在alert
"""

    def implicit_waiting(self,locationType,locatorExpression,*args):
        try:






if __name__ == '__main__':
    # WebOpen.WebStart()
    # Open126()
    # Openbaidu()
    # WebelementFunction()
    # Yunpan360()
    # ControlMouse()

    waitUtil = WaitUtil(driver)
    driver.get("http://www.baidu.com")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"kw")))    #注意(By.ID,"kw")用括号括起来了
    wv = waitUtil.visibility_element_located("id", "kw").send_keys("selenium")



    print("Over")
