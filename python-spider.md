
<!-- vim-markdown-toc GFM -->

* [Spider(网络爬虫)](#spider网络爬虫)
    * [builtwith(查看web技术)](#builtwith查看web技术)
    * [python-whois(查看web所有者)](#python-whois查看web所有者)
    * [robotparser(解析robots.txt)](#robotparser解析robotstxt)
    * [bs4(解析html)](#bs4解析html)
    * [webbrowser(打开网页)](#webbrowser打开网页)
* [web](#web)
    * [PyWebIO: 快速生成html](#pywebio-快速生成html)
* [自动化测试](#自动化测试)
    * [selenium](#selenium)
        * [虚拟图形界面](#虚拟图形界面)
        * [基本操作](#基本操作)
        * [定位element](#定位element)
        * [显式(explicit), 隐式(implicit)等待](#显式explicit-隐式implicit等待)
        * [鼠标与键盘操作](#鼠标与键盘操作)
        * [other](#other)
        * [弹窗](#弹窗)
        * [远程连接](#远程连接)
        * [unnitest](#unnitest)
        * [grid with docker](#grid-with-docker)
    * [playwright](#playwright)
    * [Puppeteer](#puppeteer)
    * [appium](#appium)
    * [airtest](#airtest)
    * [poco](#poco)

<!-- vim-markdown-toc -->
# Spider(网络爬虫)

## builtwith(查看web技术)

```py
import builtwith
url = 'https://www.jianshu.com'
builtwith.parse(url)
```

## python-whois(查看web所有者)

```py
import whois
url = 'https://www.jianshu.com'
whois.whois(url)
```

## robotparser(解析robots.txt)

```py
from urllib import robotparser
parser = robotparser.RobotFileParser()
parser.set_url('https://www.taobao.com/robots.txt')
parser.read()
parser.can_fetch('Baiduspider', 'http://www.taobao.com/article')
```

## bs4(解析html)

- [官方文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

| soup的方法, 属性 | 内容                |
|------------------|---------------------|
| soup.标签        | 第一个标签(tag类)   |
| soup.children    | 子标签 (生成器list) |
| soup.strings     | 所有文本(生成器)    |

```py
import requests
url = 'https://www.baidu.com/'
r = requests.get(url)

import bs4
soup = bs4.BeautifulSoup(r.content.decode())

# 获取第一个a标签(tag类)
tag = soup.a
```

- `tag类`属性操作和`dict`一样

 | tag类的方法, 属性               | 内容                                 |
 |---------------------------------|--------------------------------------|
 | tag.attrs                       | 查看字典                             |
 | tag.text                        | 文本(str)                            |
 | tag.content                     | 文本(list)                           |
 | tag.string.replace_with('闻新') | 更改文本                             |
 | tag.append('test')              | 添加文本                             |
 | tag.clear()                     | 清除文本                             |
 | tag.extract()                   | 去除标签                             |
 | tag['href']                     | 获取值(如果值有多个, 返回类型为list) |
 | tag.parent                      | 父标签                               |
 | tag.parents                     | 递归所有父标签(生成器)               |
 | tag.children                    | 递归所有子标签(生成器)                               |
 | tag.next_siblings               | 之后的兄弟标签(生成器)               |
 | tag.previous_siblings           | 之前的兄弟标签(生成器)               |
 | tag.next_elements               | 之后解析的对象(生成器)               |
 | tag.previous_elements           | 之前解析的对象(生成器)               |
 | tag.prettify()                  | 加上换行符,显示更直观                |
 | tag.has_attr('class')           | 是否有class属性                      |

- soup.select(): CSS选择器

```py
# 匹配第一个div标签
soup.div

# 匹配所有div标签
soup.select('div')

# 匹配div内的img
soup.select('div  img')
soup.select('div > img')

# 匹配css class
soup.select('.classname')

# 匹配id name
soup.select('#idname')

# 匹配a标签, 并且class=btn
soup.find_all("a", {"class": "btn"})

# get('id')
se = soup.select('div > p')
se[0].get('id')
```

- soup.find_all()

```py
# 匹配a标签
soup.find_all('a')

# 限制(返回list)
soup.find_all("a", limit=1)
# 等同于(返回tag类)
soup.find("a")

# 传入list同时匹配img, a标签
soup.find_all(['img','a'])

# 在div标签下找a标签
soup.div.find_all('a')

# 在div标签下找a标签, 不递归子标签
soup.div.find_all('a', recursive=False)

# 匹配id=kw
soup.find_all(id='kw')

# 匹配a标签, class=cp-feedback
soup.find_all("a", class_="cp-feedback")

# 指定属性匹配
soup.find_all(attrs={"class": "mnav"})

# 匹配所有字符串
soup.find_all(string=True)

# 匹配指定字符串
soup.find_all(string=["地图", "贴吧", "登录"])
```

- soup.find_all() 自定义函数

```py
# 匹配包含class属性, 但不包含id属性
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

soup.find_all(has_class_but_no_id)

# 匹配包含只有6个字符的class
def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6

soup.find_all(class_=has_six_characters)
```

- 其它

```py
# a标签的div父标签
soup.a.string.find_parent('div')

# a标签下一个兄弟标签
soup.a.find_next_sibling('a')

# a标签之后的兄弟标签
soup.a.find_next_siblings('a')

# a标签之后的所有a标签
soup.a.find_all_next('a')

# a标签之后的所有字符串
soup.a.find_all_next(string=True)
```


- 获取百度页面下的所有url

```py
import requests, bs4

url = 'https://www.baidu.com/'
r = requests.get(url)

soup = bs4.BeautifulSoup(r.content.decode())
a = soup.select('a')

for i in a:
    print(i.get('href'))
```

## webbrowser(打开网页)

```py
import webbrowser

# 打开网页
url = 'http://www.python.org'
webbrowser.open(url)

# 返回浏览器对象
controller = webbrowser.get()

# 浏览器程序名
controller.name

# 打开网页
controller.open(url)
```

# web

## [PyWebIO: 快速生成html](https://github.com/pywebio/PyWebIO)

# 自动化测试

- 不同框架的性能测试:

    - [Puppeteer vs Selenium vs Playwright, a speed comparison](https://blog.checklyhq.com/puppeteer-vs-selenium-vs-playwright-speed-comparison/)

    - [Cypress vs Selenium vs Playwright vs Puppeteer speed comparison](https://blog.checklyhq.com/cypress-vs-selenium-vs-playwright-vs-puppeteer-speed-comparison/)

## selenium

- [selenium官网介绍](https://www.selenium.dev/documentation/webdriver/understanding_the_components/)

- [selenium-python文档](https://selenium-python.readthedocs.io/getting-started.html)

- [python模拟登陆一些大型网站](https://github.com/Kr1s77/awesome-python-login-model)

- selenium使用基于json格式的协议与webdirver通信

- webdriver.Chrome()的方法,属性

    | 浏览器相关                     | 内容         |
    | ------------------------------ | ------------ |
    | current_window_handle          | 当前窗口句柄 |
    | window_handles                 | 所有窗口句柄 |
    | switch_to.window()             | 切换窗口句柄 |
    | close()                        | 关闭窗口     |
    | quit()                         | 关闭浏览器   |
    | forward()                      | 前进         |
    | back()                         | 后退         |
    | refresh()                      | 刷新         |
    | get()                          | 当前窗口打开url|

    | 网页相关                        | 内容         |
    | ------------------------------- | ------------ |
    | get_cookies()                   | 获取cookies  |
    | add_cookies()                   | 添加cookies  |
    | current_url                     | 当前url      |
    | title                           | 当前title    |

    | 输入框文本相关                 | 内容 |
    |------------------------------- | ---- |
    | clear()                        | 清空 |
    | send_keys()                    | 输入 |

### 虚拟图形界面

- 没有图形界面运行selenium

```sh
# 安装虚拟图形界面
# arch
pacman -S xorg-server-xvfb
# ubuntu
apt-get install xvfb

# 启动
sudo Xvfb :123
```

### 基本操作

```py
from selenium import webdriver

url = 'https://www.baidu.com/'

driver = webdriver.Chrome()
driver.get(url)
driver.quit()
# 等同于
with webdriver.Chrome() as driver:
    driver.get(url)

# 获取浏览器分辨率
size = driver.get_window_size()
width1 = size.get("width")
height1 = size.get("height")
print(width1)
print(height1)

# 设置分辨率
driver.set_window_size(1024, 768)

# 最大化
driver.maximize_window()

# 最大化
driver.minimize_window()

# 全屏F11
driver.fullscreen_window()

# 截图
driver.save_screenshot('/tmp/image.png')

# 标签截图
ele = driver.find_element_by_id("kw")
ele.send_keys("python")
ele.screenshot('/tmp/image.png')

# 切换窗口
handles = driver.window_handles          #获取当前浏览器的所有窗口句柄
driver.switch_to.window(handles[-1])     #切换到最新打开的窗口
driver.switch_to.window(handles[-2])     #切换到倒数第二个打开的窗口
driver.switch_to.window(handles[0])      #切换到第一个窗口

# 打印当前页面
from selenium.webdriver.common.print_page_options import PrintOptions

print_options = PrintOptions()
print_options.page_ranges = ['1-2']

driver.get("printPage.html")

base64code = driver.print_page(print_options)

# assert的用法
assert "百度一下，你就知道" in driver.title
```

- webdriver.ChromeOptions():

```py
# 添加options
options = webdriver.ChromeOptions()
# 设置chrome目录, 保留chrome的登陆, 插件...信息
options.add_argument(r"user-data-dir=/home/tz/.config/google-chrome/")
driver = webdriver.Chrome(options = options)

# 设置目录
options.add_argument(r"user-data-dir=/home/tz/.config/google-chrome/")

# headless模式
options.add_argument("--headless")

# 设置代理proxy
proxy = '12.12.421.125:1949'
options.add_argument('--proxy-server=socks5://' + proxy)

# 设置user-agent
opts.add_argument("user-agent=whatever you want")

# 最大化
options.add_argument("--start-maximized")

# 忽略证书没有与此相关的结果
options.add_argument("--ignore-certificate-errors")

# 禁用弹出拦截
options.add_argument("--disable-popup-blocking")

# 取消沙盒模式
options.add_argument("no-sandbox")

# 禁止默认浏览器检查
options.add_argument("no-default-driver-check")

# 禁用扩展
options.add_argument("disable-extensions")

# 禁用GLSL翻译
options.add_argument("disable-glsl-translator")

# 禁用翻译
options.add_argument("disable-translate")

# 谷歌文档提到需要加上这个属性来规避bug
options.add_argument("--disable-gpu")

options.add_argument("--disable-dev-shm-usage")
# 隐藏滚动条
options.add_argument("--hide-scrollbars")

# 不加载图片
options.add_argument("blink-settings=imagesEnabled=false")

options.add_arguments("--test-type")
options.add_argument("about:histograms")
options.add_argument("about:cache")
```

### 定位element

> (这里以百度搜索框为例):

- [定位选择器速度比较](https://www.selenium.dev/documentation/webdriver/locating_elements/#tips-on-using-selectors):

    - id > css > xpath

    - link定位内部使用的是xpath选择器


| 定位属性  | css选择器                                 | 其他选择器                              |
|-----------|-------------------------------------------|-----------------------------------------|
| 标签      | find_element_by_css_selector('input')     | find_element_by_tag_name('input')       |
| id        | find_element_by_css_selector('#kw')       | find_element_by_id("kw")                |
| class     | find_element_by_css_selector('.s_ipt')    | find_element_by_class_name('s_ipt')     |
| 属性      | find_element_by_css_selector("[name=wd]") | find_element_by_name("wd")              |
| a标签     |                                           | find_element_by_link_text("学术")       |
| a标签部分 |                                           | find_element_by_partial_link_text("学") |

- xpath

- 只支持XPath 1.0

| 操作                  | 代码                                                                                |
|-----------------------|-------------------------------------------------------------------------------------|
| 绝对路径              | find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input") |
| //为相对路径, @为属性 | find_element_by_xpath("//input[@id='kw']")

- css路径定位

| 操作                      | 代码                                         |
|---------------------------|----------------------------------------------|
| 定位span标签下的input标签 | find_element_by_css_selector('span > input') |

- 嵌套定位

```py
# 在one的定位下, 进行定位
one = driver.find_element_by_css_selector("#form > span.bg.s_ipt_wr.new-pmd.quickdelete-wrap")

two = one.find_elements_by_id("kw")
two[0].send_keys('123')

# or
two = driver.find_element_by_css_selector("#form > span.bg.s_ipt_wr.new-pmd.quickdelete-wrap").find_elements_by_id("kw")
two[0].send_keys('123')

# or
driver.find_element_by_css_selector("#form > span.bg.s_ipt_wr.new-pmd.quickdelete-wrap #kw").send_keys('123')
```

- [Selenium 4的相对定位器](https://www.selenium.dev/documentation/webdriver/locating_elements/#relative-locators)

- 带**element**的函数和带**elements**的函数:
```py
# element的函数, 返回第一个匹配
ele = driver.find_element_by_tag_name('input')

# elements的函数, 以列表类型返回所有匹配
eles = driver.find_elements_by_tag_name('input')

# 遍历eles获取属性
for i in eles:
    if i.get_attribute('name') == 'wd':
```

- 标签的属性与函数

```py
# 标签名
name = driver.find_element_by_id("kw").tag_name

# 是否已经选择, 一般用于复选框
v = driver.find_element_by_id("kw").is_selected()

# 是否启用了连接的元素
v = driver.find_element_by_id("kw").is_enabled()

# 元素坐标
v = driver.find_element_by_id("kw").rect

# 样式的值
v = driver.find_element_by_id("kw").value_of_css_property('color')

# 文本
v = driver.find_element_by_id("kw").text
```

- html里嵌套html文件

- test.html
    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>iframe</title>
        </head>
        <body>
        <div class="row">
        <div class="spanll">
        <h2>frame1</h2>
        <iframe src="in.html" id="if1" width="800" height="500"</iframe>
        </div>
        </div>
        </body>
    </html>
    ```
- in.html
    ```py
    <!DOCTYPE html>
    <html>
        <head>
            <title>iframe1</title>
        </head>
        <body>
        <div class="row">
        <div class="span8">
        <h2>frame2</h2>
        <iframe src="http://soso.com" id="if2" width="600" height="400"</iframe>
        </div>
        </div>
        </body>
    </html>
    ```
    ![image](./imgs/frame.avif)

```py
# 先定位外层
driver.switch_to_frame('if1')

# 再定位内层
driver.switch_to_frame('if2')
```


### 显式(explicit), 隐式(implicit)等待

- 因为使用AJAX(异步), element出现的时间间隔会有不同

    - 如果element没有出现在DOM中, 定位函数会出现异常 `ElementNotVisibleException`

    - click()和send_keys()等鼠标, 键盘api除外, 它们是同步的


- 显式(explicit)等待

| 常用的条件函数                         |
|----------------------------------------|
| title_is                               |
| title_contains                         |
| presence_of_element_located            |
| visibility_of_element_located          |
| visibility_of                          |
| presence_of_all_elements_located       |
| text_to_be_present_in_element          |
| text_to_be_present_in_element_value    |
| frame_to_be_available_and_switch_to_it |
| invisibility_of_element_located        |
| element_to_be_clickable                |
| staleness_of                           |
| element_to_be_selected                 |
| element_located_to_be_selected         |
| element_selection_state_to_be          |
| element_located_selection_state_to_be  |
| alert_is_present                       |

```py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 显式等待, 10秒内, 每0.1秒操作一次(默认是0.5秒)直到条件为真, 超时则输出信息
# until()
WebDriverWait(driver, 10, 0.1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR , '#kw')),
        "超时")

# until_not() 直到条件为假
WebDriverWait(driver, 10, 0.1).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR , '#kw')),
        "超时")

# title
EC.title_is("百度一下，你就知道")

# element定位
EC.presence_of_element_located((By.CSS_SELECTOR , '#kw')),

# element可点击
EC.element_to_be_clickable((By.XPATH, "//div"))
```

- 自定义函数

```py
class element_css_print(object):
  def __init__(self, css):
    self.css = css

  def __call__(self, driver):
    element = driver.find_element_by_css_selector(self.css)
    # 加入print信息
    print('抢购中')
    if element.click():
        return element
    else:
        return False

# 每0.1秒执行一次
wait = WebDriverWait(driver, 10, 0.1)
element = wait.until(element_css_print(#pro-operation > a > span))
```

- 隐式(implicit)等待

```
# 等待1秒
driver.implicitly_wait(1)
```

### 鼠标与键盘操作

- 键盘
```py
from time import sleep

driver.find_element_by_id("kw").send_keys("python")
# or
framse = driver.find_element_by_id("kw")
framse.send_keys("python")
sleep(1)

framse.send_keys(Keys.DOWN)
framse.send_keys(Keys.RETURN)

driver.find_element_by_id("kw").send_keys("python" + Keys.ENTER)

# 按ctrl-a
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()

# 清除输入的文本
driver.find_element_by_id("kw").clear()
```

- 鼠标
```py
# 表单提交
driver.find_element_by_id("").submit()

# 点击
driver.find_element_by_id("kw").click()

# 导入函数
from selenium.webdriver import ActionChains

# 悬停
ActionChains(driver).move_to_element(ele).perform()

# 双击
ActionChains(driver).double_click(ele).perform()

# 右键
ActionChains(driver).context_click(ele).perform()

# 拖拽
ActionChains(driver).drag_and_drop(ele, ele1).perform()
```

### other

```py
# 运行js
# 下拉200个像素
js = "window.scrollTo(0,200);"
# 滚动到底部
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)

# add cookies
cookie = {'name' : 'foo', 'value' : 'bar'}
driver.add_cookie(cookie)
driver.get_cookies()
```

- 高亮标签
```py
import time

def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    # 先黄后红, 最后复原
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(1)
    apply_style("background: red; border: 2px solid red;")
    time.sleep(1)
    apply_style(original_style)


driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

# 高亮搜索框
ele = driver.find_element_by_id("kw")
highlight(ele)
```

### 弹窗

- test.html
    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>弹窗test</title>
        </head>
        <body>
            <input type="button" value="alert" id="alert" onclick = "alert('alert test')"/>
            <input type="button" value="confirm" id="confirm" onclick = "confirm('confirm test')"/>
            <input type="button" value="prompt" id="prompt" onclick = "var name" = prompt('typing test:','test');document.write(name);*/>
        </body>
    </html>
    ```

- `driver.switch_to.alert` 获取弹窗对象
```py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("file:/home/tz/test.html")
driver.find_element_by_id("alert").click()

# 获取弹窗内容
driver.getText()
# 点击alert
alert = driver.switch_to.alert
# 关闭alert
alert.accept()

sleep(1)
# confirm
driver.find_element_by_id("confirm").click()
# 点击confirm
confirm = driver.switch_to.alert
# 确认confirm
confirm.accept()
# 取消confirm
confirm.dismiss()

sleep(1)
# prompt
driver.find_element_by_id("prompt").click()
# 点击prompt
prompt = driver.switch_to.alert
prompt.send_keys('test')
# 关闭prompt
prompt.accept()
# 取消confirm
prompt.dismiss()
```

### 远程连接

```sh
# archlinux 安装selenium-server-standalone
yay -S selenium-server-standalone

# 启动selenium-server-standalone
java -jar /usr/share/selenium-server/selenium-server-standalone.jar
```

```py
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

# 远程上传文件
from selenium.webdriver.remote.file_detector import LocalFileDetector

driver.file_detector = LocalFileDetector()
driver.get("http://sso.dev.saucelabs.com/test/guinea-file-upload")
driver.find_element(By.ID, "myfile").send_keys("file")
```
### unnitest

> unittest是一个基于Java JUni的内置Python模块

- 加入函数`setUp()`(初始化), `tearDown()`(收尾)
```py
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 继承unittest.TestCase
class BaiduSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.baidu.com")
        self.assertIn("百度一下，你就知道", driver.title)
        elem = driver.find_element_by_name("wd")
        elem.send_keys("python")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```

- PageObject设计模式
```py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.baidu.com/'
        self.timeout = 15

    def get(self):
        self.driver.get(self.url)

    # 使用id定位
    def find_element(self, id):
        return self.driver.find_element(By.ID, id)


class SearchPage(BasePage):
    # 搜索框和搜索按键的id
    key_id = ('kw')
    submit_id = ('su')

    def key(self, text):
        self.find_element(self.key_id).clear()
        self.find_element(self.key_id).send_keys(text)

    def submit(self):
        self.find_element(self.submit_id).click()

    def test_search(self, driver, text, expect):
        self.get()
        self.key(text)
        self.submit()

        sleep(1)
        assert(expect not in driver.page_source)


# 继承unittest.TestCase
class baidu_search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.Spage = SearchPage(self.driver)

    def test_cn(self):
        self.Spage.test_search(self.driver, '中文', '没有与此相关的结果')

    def test_en(self):
        self.Spage.test_search(self.driver, 'english', '没有与此相关的结果')

    def tearDown(self):
        self.driver.close()

def suite():
    baidu = baidu_search
    # 只测试带test的函数
    return unittest.makeSuite(baidu, "test")


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

- 在以上代码的基础上进行修改, 使用`HtmlTestRunner`生成html文件的测试报告(不知道为何, 我这个HtmlTestRunner报告很简陋)

    - 还有其它的`HtmlTestRunner`加强版

```py
from HtmlTestRunner import HTMLTestRunner

# def suite():
#     baidu = baidu_search
#     # 只测试带test的函数
#     return unittest.makeSuite(baidu, "test")


if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(suite())

    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(baidu_search))

    with open('/tmp/demo.html', 'w') as file:
        runner = HTMLTestRunner(stream=file, verbosity=2)
        runner.run(suite)
```

### grid with docker

- docker
```sh
# 下载镜像, debug版本可以使用vncviewer进行连接
docker pull selenium/hub
docker pull selenium/node-chrome-debug
docker pull selenium/node-firefox-debug

# 运行
docker run -p 4444:4444 -d --name hub selenium/hub
docker run -d -P -p 5900:5900 --name chromenode selenium/node-chrome-debug
docker run -d -P -p 5901:5900 --name firefoxnode selenium/node-firefox-debug

# 打开grid网站
http://127.0.0.1:4444/

# 停止运行
dc rm -v chromenode
dc rm -v firefoxnode
dc rm -v hub
```

- ?? 连接gird
```py
from selenium import webdriver

# 连接gird
driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub')
driver.get('https://www.baidu.com/')
driver.save_screenshot('/tmp/test.png')
driver.close()
```

- ?? 加入线程测试
```py
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.desired_capabilities import DesireCapabilities
from time import sleep

def baidu_search(host, browser):
    # caps = { 'broserName': browser }
    driver = webdriver.Remote(command_executor=host)
    driver.get('https://www.baidu.com/')
    driver.find_element_by_id("kw").send_keys('test')
    driver.find_element_by_id("su").click()
    driver.save_screenshot('/tmp/' + browser + '.png')
    sleep(3)
    # driver.close()

if __name__ == "__main__":
    pcs = {'http://127.0.0.1:4444/wd/hub' : 'chrome',
            'http://127.0.0.1:4444/wd/hub' : 'firefox'}

    threads = []
    tds = range(len(pcs))

    for host, browser in pcs.items():
        t = Thread(target=baidu_search, args=(host, browser))
        threads.append(t)

    for i in tds:
        threads[i].start()

    for i in tds:
        threads[i].join()
```


## [playwright](https://github.com/microsoft/playwright-python)

- 测试脚本与web元素交互之前，UI会在后端准备好了

- 其它框架需要写显示等待(explicit wait), 而playwright 可以自动等待

    - playwright 会对所有元素进行检查, 检查通过后, 才会执行操作

- 并行测试, 一个浏览器实例, 可以进行多个web测试

- 默认情况下, 使用headless模式

## [Puppeteer]()

- 只支持chrome浏览器

## [appium]()

- [appium-desktop:gui服务端](https://github.com/appium/appium-desktop/releases)

    - [appium-inspector:独立的inspector ui](https://github.com/appium/appium-inspector/releases)

- [python客户端](https://github.com/appium/python-client)

- python安装
```sh
pip install Appium-Python-Client
```

## [airtest](https://github.com/AirtestProject/Airtest)

- [ x ] android
- [ x ] ios
- [ x ] windows

- [官方文档](https://airtest.readthedocs.io/zh_CN/latest/README_MORE.html#getting-started)

- [api](https://airtest.readthedocs.io/zh_CN/latest/all_module/airtest.core.api.html)

- 连接android设备
```py
from airtest.core.api import *

# connect an android phone with adb
init_device("Android")
# or use connect_device api
connect_device("Android:///")

dev = device()
```
- 属性
```py
# 是否亮屏
dev.is_screenon()
# 是否锁屏
dev.is_locked()

# ip地址
dev.get_ip_address()

# activity
dev.get_top_activity()
# activity name
dev.get_top_activity_name()

# 键盘是否启用
dev.is_keyboard_shown()

# 输出分辨率等信息
dev.get_display_info()
# 只输出分辨率
dev.get_current_resolution()

# 录屏, 码率等级为1
dev.start_recording(bit_rate_level=1)
sleep(10)
dev.stop_recording(output="test.mp4")
```

- app
```py
# 启动微信
start_app("com.tencent.mm")

# 终止微信
stop_app("com.tencent.mm")

# 查看微信是否存在
check_app("com.tencent.mm")

# 查看微信路径
dev.path_app("com.tencent.mm")

# 查看所有app
dev.list_app()

# 查看第三方app
dev.list_app(third_only=True)

# 清除应用数据
clear_app(package)
```

- 鼠标与键盘操作
```py
# 模拟点击
touch((100, 100))

# 点击两次
touch((100, 100), times=2)

# touch(Template("test.png"))

# 缩小操作
pinch()

# 放大操作
pinch('out', center=(100, 100))

# 滑动
swipe((100, 100), (1000, 100))

# 返回键
keyevent("BACK")

# home键
home()

# 输入文本
text("test")

# 输入文本, 并搜索
text("test", search=True)
```

- other
```py
# shell命令
shell('ls')

# 截图
snapshot('test.png')
```

## [poco](https://github.com/AirtestProject/Poco)

- [ x ] android
- [ x ] ios
- [ x ] windows
- [ x ] macos
- [ x ] Unity3D

- [官方文档](https://poco-chinese.readthedocs.io/en/latest/)

```sh
pip install pocoui
```
