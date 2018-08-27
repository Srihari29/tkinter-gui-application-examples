#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as gui
from tkinter import messagebox

class InitMenu:
    """主界面菜单"""

    def __init__(self, master):
        """初始化菜单"""
        self.page = master
        self.root = master.page

        # 创建菜单栏
        self.menubar = gui.Menu(self.root)

        # 将菜单栏添加到窗口
        self.root.config(menu=self.menubar)

        # 文件下拉菜单
        filemenu = gui.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="新建", command=self.file_new)
        filemenu.add_command(label="打开", command=self.file_open)
        filemenu.add_command(label="保存", command=self.file_save)
        filemenu.add_command(label="另存为", command=self.file_save)
        filemenu.add_separator()
        filemenu.add_command(label="退出", command=self.root.quit)

        # 用户下拉菜单
        usermenu = gui.Menu(self.menubar, tearoff=0)
        usermenu.add_command(label="用户列表", command=self.page.open_user_list)
        usermenu.add_command(label="用户添加", command=self.page.open_user_add)
        usermenu.add_command(label="用户详情窗口", command=self.page.open_user_info)

        # 文章下拉菜单
        articlemenu = gui.Menu(self.menubar, tearoff=0)
        articlemenu.add_command(label="文章查询", command=self.page.open_content_list)
        articlemenu.add_command(label="文章添加", command=self.page.open_content_add)
        articlemenu.add_command(label="文章统计", command=self.page.open_content_count)

        # 数据下拉菜单
        datamenu = gui.Menu(self.menubar, tearoff=0)
        datamenu.add_command(label="下载", command=self.page.openDownload)
        datamenu.add_command(label="上传", command=self.page.openUpload)
        datamenu.add_command(label="同步", command=self.page.openSynchronize)
        datamenu.add_command(label="备份", command=self.page.openBackup)

        # 帮助下拉菜单
        helpmenu = gui.Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="欢迎使用", command=self.help_about)
        helpmenu.add_command(label="文档", command=self.help_about)
        helpmenu.add_command(label="版权声明", command=self.help_about)
        helpmenu.add_command(label="隐私声明", command=self.help_about)
        helpmenu.add_separator()
        helpmenu.add_command(label="联系我们", command=self.page.open_ontact)
        helpmenu.add_command(label="关于", command=self.page.open_about)

        # 将下拉菜单加到菜单栏
        self.menubar.add_cascade(label="文件", menu=filemenu)
        self.menubar.add_cascade(label="用户", menu=usermenu)
        self.menubar.add_cascade(label="文章", menu=articlemenu)
        self.menubar.add_cascade(label="数据", menu=datamenu)
        self.menubar.add_cascade(label="帮助", menu=helpmenu)

    def file_open(self):
        messagebox.showinfo("打开", "文件-打开！")  # 消息提示框
        pass

    def file_new(self):
        messagebox.showinfo("新建", "文件-新建！")  # 消息提示框
        pass

    def file_save(self):
        messagebox.showinfo("保存", "文件-保存！")  # 消息提示框
        pass

    def edit_cut(self):
        messagebox.showinfo("剪切", "编辑-剪切！")  # 消息提示框
        pass

    def edit_copy(self):
        messagebox.showinfo("复制", "编辑-复制！")  # 消息提示框
        pass

    def edit_paste(self):
        messagebox.showinfo("粘贴", "编辑-粘贴！")  # 消息提示框
        pass

    def help_about(self):
        """关于"""
        messagebox.showinfo(
            "关于", "作者: doudoudzj \n verion 1.0 \n 感谢您的使用！ \n doudoudzj@sina.com"
        )

class initLoginMenu:
    """登陆界面菜单"""
    def __init__(self, master):
        self.root = master

        # 创建菜单栏
        menubar = gui.Menu(self.root)
        # 创建“文件”下拉菜单
        filemenu = gui.Menu(menubar, tearoff=0)
        # 添加菜单项
        filemenu.add_command(label="退出", command=self.root.quit)
        # 将下拉菜单加到菜单栏
        menubar.add_cascade(label="文件", menu=filemenu)
        # 将菜单栏整个加到窗口
        self.root.config(menu=menubar)
