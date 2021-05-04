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

## selenium(控制浏览器)

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

    | 网页相关                       | 内容         |
    |------------------------------- | ------------ |
    | get_cookies()                  | 获取cookies  |
    | add_cookies()                  | 添加cookies  |
    | current_url                    | 当前url      |
    | title                          | 当前title    |

    | 输入框文本相关                 | 内容 |
    |------------------------------- | ---- |
    | clear()                        | 清空 |
    | send_keys()                    | 输入 |

- 定位方法

```py
from selenium import webdriver

# 需要安装chromedriver
browser = webdriver.Chrome()

url = 'https://www.baidu.com/'
browser.get(url)

# 通过'标签名'定位搜索框
??browser.find_element_by_css_selector('input')

# '#idname' 通过id定位搜索框
browser.find_element_by_css_selector('#kw')
# or
browser.find_element_by_id("kw")

# '.classname' 通过class定位搜索框
browser.find_element_by_css_selector('.s_ipt')
# or
browser.find_element_by_class_name('s_ipt')

# 定位span标签下的input标签
browser.find_element_by_css_selector('span > input')

# 通过属性定位
browser.find_element_by_css_selector("[autocomplete=off]")
browser.find_element_by_css_selector("[name=wd]")

# 通过xpath定位, //为相对路径
browser.find_element_by_xpath("//input[@id='kw']")
```

- 模拟点击, 输入

```py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
url = 'https://www.baidu.com/'
browser.get(url)

# 以上方法定位搜索框后输入python, 再输出搜索个数
framse = browser.find_element_by_id("kw")
framse.send_keys("python")
framse.send_keys(Keys.RETURN)
print(browser.find_element_by_css_selector(".nums_text").text)

# link_text().click()点击学术链接
browser.find_element_by_link_text("学术").click()

# 鼠标悬停
from selenium.webdriver import ActionChains
above = browser.find_element_by_link_text("更多")
ActionChains(browser).move_to_element(above).perform()

# 打开学术, 视频, 新闻后, 切换窗口至学术
cur = browser.current_window_handle
browser.find_element_by_link_text("学术").click()
browser.find_element_by_link_text("视频").click()
browser.find_element_by_link_text("新闻").click()
browser.switch_to.window(cur)

# 运行js
js = "window.scrollTo(200,850);"
browser.execute_script(js)

# add cookkies
cookie = {'name' : 'foo', 'value' : 'bar'}
browser.add_cookie(cookie)
browser.get_cookies()
```
