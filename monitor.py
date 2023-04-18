from qdoj import getStatus
import csv
import tkinter as tk
import threading
import time
# 不存在的id?
# 修改roomid和cid
roomid = 418  # 这个是用来指定房间号
cid = 5  # 这个是用来指定比赛id

vis = {}  # 用来保存哪些提交已经发过气球的了
doing = {}  # 用来保存当前显示的提交的，用来防止有人一道题多次提交
data = {}  # 用来保存每个用户的房间号和座位号
todo = []  # 用来保存还没有发放气球的用户列表

win = tk.Tk()
win.title('发好气球后点击按钮')
win.geometry('640x320')


class User:

    def __init__(self, name, rid):
        self.b = tk.Button(win,
                           text=name,
                           width=30,
                           height=2,
                           command=self.destroy)
        self.b.pack()
        self.rid = rid

    def destroy(self):
        vis[self.rid] = 1
        with open('tmp.csv', 'a', newline='') as f:
            f.write(self.rid + '\n')

        self.b.destroy()


def updataStatus(page):
    global todo
    status_list, n = getStatus(cid, page, '', '', 0)
    for p in status_list:
        userName = str(p['userName'])
        pid = str(p['problemID'])
        rid = userName + '_' + pid
        print(userName, pid)
        if userName not in data:
            with open('error.csv', 'a', newline='') as f:
                f.write(userName + ',' + pid + '\n')
        else:
            if rid not in vis and data[userName][0] == str(
                    roomid) and rid not in doing:
                doing[rid] = True
                todo.append(
                    User('题号:' + pid + ' ' + '座位号:' + data[userName][1], rid))


try:
    with open('tmp.csv', 'r') as f:
        '''
        tmp.csv 保存的是已经发过气球的名单
        包括：用户名+题目id
        '''
        for l in f:
            vis[l[:0]] = True
except FileNotFoundError:
    pass

with open('tot.csv', 'r') as f:
    '''
    需要另外一个 data.csv 存储所有比赛选手的个人信息，至少包括
    用户名，房间号，座位号
    '''
    file_csv = csv.reader(f)
    for p in file_csv:
        print(p[6])
        data[p[6]] = (p[8], p[9])

# 第一次读榜，全读
_, tot = getStatus(cid, 1, '', '', 0)
page = int((tot + 49) / 50)
for i in range(page):
    updataStatus(i + 1)


def job():
    while True:
        updataStatus(1)
        time.sleep(5)  # 5秒读一次


threading.Thread(target=job).start()

win.mainloop()