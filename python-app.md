# pymupdf(pdf, epub)

- [微信:Python处理PDF——PyMuPDF的安装与使用]()

```py
import fitz

# 打开文档
doc = fitz.open("./name.pdf")

# 获取目录
toc = doc.get_toc()

# get_text()默认为文本
page = doc[0]
page.get_text()
page.get_text("blocks") # 以\n分段
page.get_text("words")  # 以单词分段
page.get_text("html")   # html

# 搜索文本，返回矩阵
areas = page.search_for("text")

# 打印所有页面文本
for page in doc:
    print(page.get_text())


# 保存第一页为图片
page = doc[0]
pix = page.get_pixmap()
pix.save("page-%i.png" % page.number)

# 合并文档。文档必须是同一格式，如果是pdf合并epub就会报错
doc.insert_pdf(doc1)

# 拆分
doc2 = fitz.open()
doc2.insert_pdf(doc, to_page = 9) # 插入前10页
doc2.save("new.pdf")

# 关闭缓冲区
doc.close()
```

# Image

- [官方文档](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)

```py
from PIL import Image
image = Image.open('/tmp/test.jpg')

# 裁剪
rect = 80, 20, 500, 550
image.crop(rect).show()

# 缩略
size = (128, 128)
# image.thumbnail(size)

# 旋转
image.rotate(180).show()

# 翻转
image.transpose(Image.FLIP_LEFT_RIGHT).show()

# 滤镜
from PIL import ImageFilter
image.filter(ImageFilter.CONTOUR).show()
```
### pynput.keyboard(自动输入)

```py
# 键盘
from pynput.keyboard import Key, Controller

keyboard = Controller()

# 按一下enter
keyboard.press(Key.enter)

# 按住c
keyboard.release('c')


# 鼠标
from pynput.mouse import Button, Controller as MouseController
mouse = MouseController()
```


# pyautogui(自动化键盘, 鼠标)

- 键盘

```py
import pyautogui

# 输入
pyautogui.typewrite('Hello world!')
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

# keyDown()按住, keyUp()送开
pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

# 输入Ctrl-C
pyautogui.hotkey('ctrl', 'c')
```

- 鼠标

```py
# 获取分辨率
pyautogui.size()

# 获取鼠标坐标
pyautogui.position()

# 在100, 150位置,点击左键
pyautogui.click(100,150,button='left')

# 在100, 150位置,点击右键
pyautogui.click(100,150,button='right')

# 双击
pyautogui.doubleClick()

# 鼠标滚动
pyautogui.scroll(200)

# 鼠标向右移动100
pyautogui.moveRel(100, 0, duration=0)

# 拖住移动0.25秒
pyautogui.dragRel(100, 0, duration=0.25)

# 鼠标向下移动100
pyautogui.moveRel(0, 100, duration=0)

# 鼠标向左移动100
pyautogui.moveRel(-100, 0, duration=0)

# 鼠标向上移动100
pyautogui.moveRel(0, -100, duration=0)
```

- 图片

```py
# 获取图片, 需要安装scrot
im = pyautogui.screenshot()

# 读取本地图片
pyautogui.locateOnScreen('123.png')

# 获取像素RGB
im.getpixel((0, 0))
```

# [wxpy: 微信自动化](https://github.com/youfou/wxpy)

- [官方文档](https://wxpy.readthedocs.io/zh/latest/)

- 好友

```py
from wxpy import *
# 登陆微信
bot = Bot()

# 查看所有好友
bot.friends()

# 查看所有好友信息
bot.friends().stats_text()

# 查找好友
my_friend = bot.friends().search('name')[0]

# 发送信息
my_friend.send('Hello, WeChat!')
# 发送图片
my_friend.send_image('my_picture.png')
# 发送视频
my_friend.send_video('my_video.mov')
# 发送文件
my_friend.send_file('my_file.zip')
# 以动态的方式发送图片
my_friend.send('@img@my_picture.png')('my_picture.jpg')

# 下载好友头像
img = my_friend.get_avatar()
with open('img.png','wb') as file:
     file.write(img)

# 下载所有好友的头像
for friend in bot.friends():
    img = friend.get_avatar()
    with open(f'{friend.name}.png','wb') as file:
         file.write(img)
```

- 群

```py
# 查看群
bot.groups()

# 查找群
group = bot.groups().search('name')[0]

# 查看群主
group.owner

# 查看群友
for i in group:
    print(i)

# 查看好友是否在群里
my_friend in group

# 查看所有公众号
bot.mps()
```
- 统计好友地区分布

```py
# 获取好友信息
friends_stat = bot.friends().stats()

# 统计好友地区分布
friend_list = []
for province, count in friends_stat["province"].items():
    if province != "":
        friend_list.append([province, count])

# 排序
friend_list.sort(key=lambda x: x[1], reverse=True)

# 打印
for item in friend_list[:10]:
     print(item[0], item[1])
```

- 对以上的统计例子, 使用`pyecharts`生成饼图

```py
from pyecharts.charts import Pie
from pyecharts import options as opts

# 生成饼图
(
    Pie()
    .add("", friend_list)
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts())
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("name.html")
)
```

- 统计好友男女数量

```py
for sex, count in friends_stat["sex"].items():
    # 1代表MALE, 2代表FEMALE
    if sex == 1:
        print("MALE %d" % count)
    elif sex == 2:
        print("FEMALE %d" % count)
```

- 对以上的统计例子, 使用`pyecharts`生成饼图

```py
friends_stat = bot.friends().stats()

sex_list = []
for sex, count in friends_stat["sex"].items():
    # 1代表男, 2代表女
    if sex == 1:
        sex_list.append(['男', count])
    elif sex == 2:
        sex_list.append(['女', count])

# 生成饼图
from pyecharts.charts import Pie
from pyecharts import options as opts
(
    Pie()
    .add("", sex_list)
    .set_colors(["blue", "red"])
    .set_global_opts(title_opts=opts.TitleOpts())
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("name.html")
)
```

- 其它功能

```py
# 打印好友, 群公众号信息
@bot.register()
def print_others(msg):
    print(msg)

# 自动回复
@bot.register(mp)
def forward_message(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

# 指定好友, 自动回复
@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)
```

- 图灵机器人自动回复消息

```py
import json
import requests

# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "你的api key"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "123456"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "[tuling] " + result["text"]

@bot.register(my_friend)
def reply_my_friend(msg):
    return auto_reply(msg.text)
```

# [pyecharts: python ECharts数据可视化](https://github.com/pyecharts/pyecharts)

- [官方文档](https://gallery.pyecharts.org/#/README)

- Bar(柱形图)
```py
from pyecharts.charts import Bar

bar = Bar()
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

# x轴
bar.add_xaxis(attr)
# y轴
bar.add_yaxis("商家A", v1)
bar.add_yaxis("商家B", v1)

# 生成html
bar.render('name.html')
```

- 链式调用

```py
from pyecharts.charts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

(
    Bar()
    # x轴
    .add_xaxis(attr)
    # y轴
    .add_yaxis("商家A", v1)
    .add_yaxis("商家B", v1)

    # 生成html
    .render('name.html')
)
```

- Line(折线图)

```py
from pyecharts.charts import Line
import pyecharts.options as opts

line = Line()
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

(
    # 设置宽度, 高度
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=attr)
    .add_yaxis(series_name="商品A", y_axis=v1,)
    .add_yaxis(series_name="商品B", y_axis=v2,)
    .render("name.html")
)
```

- 画点, 画线

```py
from pyecharts.charts import Line
import pyecharts.options as opts

line = Line()
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

(
    Line()
    .add_xaxis(xaxis_data=attr)
    .add_yaxis(series_name="商品A", y_axis=v1,
        # MarkPointOpts()高亮最大, 最小点
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ]
        ),
        # 高亮平均点
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
    .add_yaxis(series_name="商品B", y_axis=v2,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)]
        ),
        # MarkLineOpts()最高点画线
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值"),
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
                opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
            ]
        ),
    )
    .render("name.html")
)
```
- 图表转换
```py
from pyecharts.charts import Line
import pyecharts.options as opts

line = Line()
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

(
    Line()
    .add_xaxis(xaxis_data=attr)
    .add_yaxis(series_name="商品A", y_axis=v1,
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
    .add_yaxis(series_name="商品B", y_axis=v2,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值"),
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
                opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
            ]
        ),
    )
    # 图表转换
    .set_global_opts(
        title_opts=opts.TitleOpts(title="标题", subtitle="子标题"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("name.html")
)
```

- Pie(饼图)

```py
from pyecharts.charts import Pie
from pyecharts import options as opts

data = [['小米', 65], ['三星', 83], ['华为', 20], ['苹果', 116], ['魅族', 44], ['VIVO', 96], ['OPPO', 92]]

phones = (
    Pie()
    .add("", data)
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("name.html")
)
```

# [Diagrams: 生成架构图](https://github.com/mingrammer/diagrams)
