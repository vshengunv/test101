# 导入selenium的webdriver模块
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 导入chrome.service模块
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

# 跨目录调用文件
import sys
from  os.path import dirname,abspath
project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path + "\\module")
# 详情解释见invocation_file文件，这里是调用了其中的add方法
from cat_game.invocation_file import add
try:
    c2 = add(1,5)
    print(c2)
# 不在异常处中断程序，而是在此处打印信息通知作者此处异常
except BaseException:
    print("调用add函数异常")
# 让python直接来告诉我们异常原因以及信息
except BaseException as msg:
    print(msg)
else:
    print("调用add函数正常")
finally:
    print("不论add函数调用是否异常，此信息都将被打印")

'''
Pip 的常用命令如下。
> pip install selenium   #安装selenium

> pip install selenium==3.11.0 # 安装指定版本号

> pip install -U selenium # 安装最新版本号

> pip show selenium # 查看当前包的版本信息

> pip uninstall selenium # 卸载 Selenium
'''     #pip的常用命令

# 打印当前时间
print("现在是北京时间：",time.ctime())

# driver = webdriver.Chrome()
driver = webdriver.Firefox()

# 设置网页最大加载时间
try:
    driver.set_page_load_timeout(3)
    driver.get("http://www.baidu.com")
except TimeoutError:
    print("timeout")

# 定位元素
# driver.find_element(By.ID,"input").send_keys("selenium")

# 利用元素属性、Xpath定位元素（利于封装）
# driver.find_element(By.ID,"kw").send_keys("Selenium")
# driver.find_element(By.XPATH,"//input[@name='wd']").send_keys("Selenium")         #通过Xpath使用元素name的属性值来定位
# driver.find_element(By.XPATH,"//input[@class='s_ipt']").send_keys("Selenium")     #通过Xpath使用元素class的属性值来定位
# driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("Selenium") #通过Xpath使用元素id的属性值来定位('*'表示不想指定标签名)

#将层级与属性结合，利用父属性定位元素
# driver.find_element(By.XPATH,"//span[@class='bg s_ipt_wr']/input")  #通过class定位到父元素，后面的/input表示父元素下面的子元素
# driver.find_element(By.XPATH,"//form[@id='form']/span/input")  #通过父父元素form定位，后面的/span/input表示对应的子元素

#结合逻辑运算符定位元素
# driver.find_element(By.XPATH,"//input[@id='kw' and @class='s_ipt']")    #and 表示必须满足两个条件来定位元素。

#使用contains方法来定位元素
# driver.find_element(By.XPATH,"//span[contains(@class,'s_ipt_wr')]/input").send_keys("Selenium") #contains方法只取了class属性中的“s_ipt_wr”部分。

#使用text()方法来定位元素
# driver.find_element(By.XPATH,"//a[text()='hao123']").click()   #text()通过匹配文本信息来定位元素hao123，然后点击跳转

#使用contains()与text()相结合来定位元素
# driver.find_element(By.XPATH,"//a[contains(text(),'hao123')]").click()  #两种方法结合定位元素，注意中间不再用‘ = ’而用’ , ‘

'''
— — — CSS选择器的常见语法 — — —
.class      	     .intro         	class选择器，选择class="intro"的所有元素
#id     	          #firstname	    id选择器，选择id="firstname"的所有元素
*                  	*	                选择所有元素
element         	p	                元素所有元素
element>element 	div>input	        选择父元素为<div>的所有<input>元素
element+element	    div+input	        选择同一级中紧接在<div>元素之后的所有<input>元素
[attribute=value]	[target=_blank]	    选择target="_blank"的所有元素。
'''         #— — CSS选择器的常见语法 — —
# CSS定位元素
driver.find_element(By.CSS_SELECTOR,'.s_ipt').send_keys("Selenium")

'''
需要先导入模块 from selenium.webdriver.common.by import By
    find_element(By.ID,"kw")
    
    find_element(By.NAME,"wd")
    
    find_element(By.CLASS_NAME,"s_ipt")
    
    find_element(By.TAG_NAME,"input")
    
    find_element(By.LINK_TEXT,"新闻")
    
    find_element(By.PARTIAL_LINK_TEXT,"新")
    
    find_element(By.XPATH,"//*[@class='bg s_btn']")
    
    find_element(By.CSS_SELECTOR,"span.bg s_btn_wr>input#su")
'''         #— — 用By定位元素（通过By声明定位方法） — —


driver.find_element(By.ID,"su").click()
time.sleep(5)
driver.quit()