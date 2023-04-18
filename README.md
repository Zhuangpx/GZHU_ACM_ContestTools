# GZHU_ACM_ContestTools

GZHU比赛工具集。

已有师兄基于[GZHUoj](https://github.com/KIDx/GzhuOJ)写过一套[工具集](https://github.com/9lie/GZHUOJContestTools)。

往后更换服务器，又用[qduoj](https://opensource.qduoj.com/#/)搭建了一个，用于新生赛和校赛。

后来组织校赛和队长在以往基础上又写了一份，于是便有了这份工具集。

## 介绍

`gzhuoj.py`提供gzhuoj的一些基本函数，注册账号，修改信息，添加账号到比赛中等。

`qdoj.py`提供了从qdoj爬status，并把结果返回。由于qdoj管理后台做的很完善，不需要重写注册等功能。

`monitor.py`是一个用来辅助发气球的脚本。
需要提供一个选手的名单表，`tot.csv`，大概是`学院|专业|班级|姓名|学号|序号|账号|密码|考室|座位`(序号也可能是预选赛排名，总之是个不重全排列)，发过气球会保存在`tmp.csv`，大概是`账号_题号`，根据窗口信息发完气球点击即可。
`error.csv`是不通过的status，没什么用。

大体上是根据[lxl师兄](https://github.com/9lie)的工具集来的，后来者也可以在这基础上修改(如果有的话)。

## 关于出题

- 应该需要一个出题群和验题群，出题人先互相验证，再由专门验题的同学二次验题，二次验题的同学尽量不要接触到出题信息。
- 出题建议先提idea，再讨论做法，最后才是数据和题面，提前写好标程和题解的备稿，保证题目真的没问题。
- 出题群应该有个共享文档，比如飞书文档(无推广)。
- 出完打上tag，建议要有备选的题目或者idea，灵活变动。
- 题目的数据需要从不同的角度考虑，尽可能考虑每种情况，不要只有随机数据。尽量从不同水平的选手出发思考他们的解题方法来构造数据
- 验题不是做了就行，当做自己在比赛反馈问题，以及尽量考虑多种情况和做法。
- 注意难度。

## 关于组织校赛

- 首先要写好推文，提前建好q群。q群写好公告和比赛信息。
- 初步报名收集好选手信息，至少包括：学院，专业，班级，学号，姓名。可以有性别（最佳女生奖？）。作为初步的名单。
- 如果有人数很多，进行线上预赛，注意题目选择以及防作弊。英文题翻成中文是个不错的选择。
- 注册好选手的比赛账号。
- 提前了解好赛场的电脑的情况，确定哪些机子有问题，然后安排座位。注意要准备几台机子备用。
- 打印好签到表和账号表，提前到场准备气球和签到，以及赛中问题答疑。
- 发气球
- 赛后不要解散q群，方便后面证明发放以及校队选拔。
- 有一个问题是同步赛，如果想要放到牛客同步赛，需要对题目更加谨慎，以及，需要腾出人生维护和答疑。

## 一些经验教训

- 出题根据选手水平来，不要太高估选手水平。
- 多找人验题，验题很重要，不要出现类似数据出错这种问题(惨痛教训)。
- 随时准备服务器重启和rejudge，尽量不要这样做，但要以防万一(gzhuoj的rejudge就有bug，惨痛教训+1)。
- 备用机子一定要留。
- 题面一定要清晰，不要当谜语人(惨痛教训+2)。
