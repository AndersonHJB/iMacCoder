---
title: Python搭建一个系统信息实时监控数据可视化大屏
tags: []
id: '1815'
categories:
  - - uncategorized
date: 2021-08-01 00:02:19
---

本文分享使用python搭建服务器应用的监控系统面板，主要流程如下： 1、数据库中创建数据表 2、建立数据库连接 实时数据插入数据表，实时查询更新面板数据准备 3、监控中心大屏制作 具体步骤： 1、创建监测指标数据表字段 这里为了方便将系统信息监控的CPU信息、内存信息、磁盘信息放在一张表中。 实际上可以将CPU和磁盘信息监控指标分表设置，两者对时间粒度要求是不一样的，减少不需要的资源消耗。后期专门写一篇来聊聊如何搭建数据指标体系。

```python
import pymysql
db = pymysql.connect(user="root", passwd="root", db="mydb", host="127.0.0.1")
cur = db.cursor()

# from sqlalchemy import create_engine
# engine = create_engine(
#     "mysql+pymysql://root:root@127.0.0.1:3306/mydb?charset=utf8")
# print(engine)


# 创建数据表--系统信息监控
sql="""CREATE TABLE IF NOT EXISTS system_info(
     ID int(8) not null auto_increment COMMENT '序号',
     TIME datetime not null COMMENT '记录时间',
     mem_free VARCHAR (100) NOT NULL COMMENT '可用内存',
     mem_total VARCHAR (100) NOT NULL COMMENT '总内存',
     mem_percent VARCHAR (100) NOT NULL COMMENT '内存百分比',
     mem_used VARCHAR (100) NOT NULL COMMENT '占用内存',
     cpu VARCHAR (100)  COMMENT 'CPU占比',
     disk1 VARCHAR (100)  COMMENT 'C盘使用占比',
     disk2 VARCHAR (100)  COMMENT 'D盘使用占比',
     disk3 VARCHAR (100)  COMMENT 'E盘使用占比',
     disk4 VARCHAR (100)  COMMENT 'F盘使用占比',
     disk5 VARCHAR (100)  COMMENT 'G盘使用占比',
     primary key(ID)
) ENGINE = INNODB DEFAULT CHARSET = utf8 COMMENT = '系统信息监控';
"""
cur.execute(sql)
cur.close()
```

图片 2、建立数据库连接 定时获取主机的一些内存、CPU、磁盘的信息，将获取的信息存储到数据库；这里利用轻量级定时模块schedule。

```python
import psutil
import time
import pymysql
from datetime import datetime
import schedule

db = pymysql.connect(user="root", passwd="root", db="mydb", host="127.0.0.1")
db.autocommit(True)
cur = db.cursor()
def Get_sys_info():
    # cpu信息
    cpu = str(psutil.cpu_percent(interval=1)) + '%'
    # cpu = psutil.cpu_percent(interval=1, percpu=True)

    # 内存信息
    mem = psutil.virtual_memory()
    mem_total = round(mem.total / 1024 / 1024 / 1024, 0)
    mem_free = round(mem.free / 1024 / 1024 / 1024)
    mem_percent = str(mem.percent) + '%'
    mem_used = round(mem.used / 1024 / 1024 / 1024)

    # 磁盘信息(磁盘空间使用占比)
    disk1 = str(psutil.disk_usage('C:/').percent) + '%'
    disk2 = str(psutil.disk_usage('D:/').percent) + '%'
    disk3 = str(psutil.disk_usage('E:/').percent) + '%'
    disk4 = str(psutil.disk_usage('F:/').percent) + '%'
    disk5 = str(psutil.disk_usage('G:/').percent) + '%'

    return mem_free,mem_total,mem_percent,mem_used,cpu,disk1,disk2,disk3,disk4,disk5

if __name__ == "__main__":

    def job():
        mem_free, mem_total, mem_percent, mem_used, cpu, disk1, disk2, disk3, disk4, disk5 = Get_sys_info()
        now_time = datetime.now()
        list1 = [now_time, mem_free, mem_total, mem_percent, mem_used, cpu, disk1, disk2, disk3, disk4, disk5]
        tuple_list = tuple([str(i) for i in list1])
        print(tuple_list)

        sql = """insert into system_info(TIME,mem_free,mem_total,mem_percent,mem_used,cpu,disk1,disk2,disk3,disk4,disk5) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        cur.execute(sql, tuple_list)

    try:
        schedule.every().minute.at(":00").do(job)

    except Exception as e:
        print('错误: %s'% e)

    while True:
        schedule.run_pending()
        time.sleep(1)
```

服务启动后，每分钟向数据库插入一次数据记录。这里有个小问题，插入时间点并没有从设置的：00开始，后面再优化这个细节。 图片 3、监控中心大屏 从数据库获取数据如服务器的内存、CPU信息等，通过Pyecharts可视化制作图表并布局看板。通过以下流程生成一个粗略的大屏布局，由7个部分组成，按顺序排列。

```python
import pymysql
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Page
from pyecharts.globals import ThemeType

db = pymysql.connect(user="root", passwd="root", db="mydb", host="127.0.0.1")
cur1 = db.cursor()
cur2 = db.cursor()
cur3 = db.cursor()

SQL1="""SELECT TIME,cpu,mem_percent FROM system_info WHERE TIME > DATE_SUB(NOW(), INTERVAL 60 MINUTE)"""  #查询最近1h内数据展示

SQL2 = 'select disk1,disk2,disk3,disk4,disk5 from system_info order by TIME desc limit 1'

SQL3 = 'select mem_free,mem_total,mem_percent,mem_used from system_info order by TIME desc limit 1'

cur1.execute(SQL1)
cur2.execute(SQL2)
cur3.execute(SQL3)
cpu_data = cur1.fetchall()
disk_data = cur2.fetchall()
mem_data = cur3.fetchall()

all_time = []
all_cpu = []
all_mem_percent = []
for time_cpu in cpu_data:
    TIME=time_cpu[0]
    cpu0=time_cpu[1].split('%')
    cpu_num = eval(cpu0[0])

    mem0=time_cpu[2].split('%')
    mem_percent = eval(mem0[0])

    all_cpu.append(cpu_num)
    all_time.append(TIME)
    all_mem_percent.append(mem_percent)

disk_list = list(disk_data[0])
disk_percent=[eval(x.split("%")[0]) for x in disk_list]

def tab0(name, color):  # 标题
    c = (Pie().
        set_global_opts(
        title_opts=opts.TitleOpts(title=name, pos_left='center', pos_top='center',
                                  title_textstyle_opts=opts.TextStyleOpts(color=color, font_size=20))))
    return c

def tab1(name, color):  # 标题
    c = (Pie().
        set_global_opts(
        title_opts=opts.TitleOpts(title=name, pos_left='center', pos_top='center',
                                  title_textstyle_opts=opts.TextStyleOpts(color=color, font_size=30))))
    return c

def tab2(name, color):
    c = (Pie().
        set_global_opts(
        title_opts=opts.TitleOpts(title=name, pos_left='center', pos_top='center',
                                  title_textstyle_opts=opts.TextStyleOpts(color=color, font_size=25))))
    return c

def line(all_time, all_cpu):
    line = (
        Line()
        .add_xaxis(all_time)
        .add_yaxis("CPU_info：%", all_cpu)
        .set_global_opts(title_opts=opts.TitleOpts(title="CPU_info"))
    )
    line.render()

    return line

def line1(all_time, all_mem_percent):
    line = (
        Line()
        .add_xaxis(all_time)
        .add_yaxis("Mem_percent：%",all_mem_percent)
        .set_global_opts(title_opts=opts.TitleOpts(title="内存使用占比"))
    )
    line.render()

    return line

def bar(disk_percent):

    bar =(Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))  #在这里输入啊，设置绘图主题为CHALK
        .add_xaxis(["C盘","D盘","E盘","F盘","G盘"])
        .add_yaxis("磁盘使用占比：%",disk_percent))
    bar.render()
    return bar


def pie_base():
    c = (
        Pie()
        .add("", [list(z) for z in zip(['mem_free', 'mem_used'],
                                       [mem_data[0][0],mem_data[0][3]])])
        .set_global_opts(title_opts=opts.TitleOpts(title="内存使用占比"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c
#将上面图拼接到网页上
page = Page()
page.add(
    tab0("Python数据分析实例", "#2CB34A"),
    line(all_time,all_cpu),
    tab1("系统信息监控数据可视化大屏", "#2CB34A"),
    tab2("可用内存:{mem_free}\n\n总内存:{mem_total}\n\n内存占比:{mem_percent}\n\n占用内存:{mem_used}".format(mem_free=mem_data[0][0],mem_total=mem_data[0][1],mem_percent=mem_data[0][2],mem_used=mem_data[0][3]), "#000000"),
    bar(disk_percent),
    pie_base(),
    line1(all_time,all_mem_percent)
)
page.render("data_center.html")
db.close()
```

配色码-查看RGB颜色查询对照表RGB颜色三原色配色表 (sojson.com) ![](https://img-blog.csdnimg.cn/img_convert/3414e05ccafcee1d7aa9a9ac3d9a4c9d.png) 数据可视化面板预览 最后，进一步对大屏布局并设置一张好看的底图。 其中，lxml是python的一个解析库，支持HTML和XML的解析。

```python
from bs4 import BeautifulSoup
with open("data_center.html", "r+", encoding='utf-8') as html:
    html_1 = BeautifulSoup(html, 'lxml')
    divs = html_1.select('.chart-container')
    divs[0]["style"] = "width:10%;height:10%;position:absolute;top:0;left:2%;"
    divs[1]["style"] = "width:40%;height:40%;position:absolute;top:12%;left:2%;"
    divs[2]["style"] = "width:35%;height:10%;position:absolute;top:1%;left:30%;"
    divs[3]["style"] = "width:40%;height:40%;position:absolute;top:10%;left:25%;"
    divs[4]["style"] = "width:40%;height:35%;position:absolute;top:12%;left:55%;"
    divs[5]["style"] = "width:30%;height:35%;position:absolute;top:60%;left:5%;"
    divs[6]["style"] = "width:60%;height:50%;position:absolute;top:50%;left:35%;"

    body = html_1.find("body")
    body["style"] = """background-image:url("./img/test.jpg")"""  # 背景图片

    html_new = str(html_1)
    html.seek(0, 0)
    html.truncate()
    html.write(html_new)
    html.close()
```

#备注：divs\[0\]\["style"\] = "width:10%;height:10%;position:absolute;top:0;left:2%;"即是我们对宽度、高度、位置、上边距、左边距的定义，这里我们用百分比以达到屏幕自适应的效果。 效果图如下： ![](https://gitee.com/huangjiabaoaiyc/image/raw/master/6mkJGwYqQ3EpDZK.jpg) 至此，一个实时系统信息监控面板开发完毕。其他功能可自行拓展，本文仅演示创建的具体流程，其他细节可进一步优化，如具体到单个应用的监测与控制。 文中包含所有代码，快动手尝试一下吧。 ![](https://gitee.com/huangjiabaoaiyc/image/raw/master/1569e12e831d1f6d9c4efb38411d43f.jpg)\]