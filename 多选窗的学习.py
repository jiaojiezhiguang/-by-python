# import wx

# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(None,title="复选框和单选按钮",size=(330,120))
#         panel = wx.Panel(parent=self)

#         st1 = wx.StaticText(panel,label="你最喜欢的编程语言：")
#         cb1 = wx.CheckBox(panel,id=1,label="Python")
#         cb2 = wx.CheckBox(panel,id=2,label="Java")
#         cb2.SetValue(True)
#         cb3 = wx.CheckBox(panel,id=3,label="C++")
#         self.Bind(wx.EVT_CHECKBOX,self.on_checkbox_click,id=1,id2=3)
        
#         st2 = wx.StaticText(panel,label="选择性别")
#         rabio1 = wx.RadioButton(panel,id=4,label="男",style=wx.RB_GROUP)
#         rabio1 = wx.RadioButton(panel,id=5,label="女")
#         self.Bind(wx.EVT_RADIOBUTTON,self.on_redio_click,id=4,id2=5)

#         hbox1 = wx.BoxSizer()
#         hbox1.Add(st1,flg=wx.LEFT|wx.RIGHT,border=5)
#         hbox1.Add(cb1)
#         hbox1.Add(cb2)
#         hbox1.Add(cb3)

#         hbox2 = wx.BoxSizer()
#         hbox2.Add(st2,flg=wx.LEFT|wx.RIGHT,border=5)
#         hbox2.Add(radio1)
#         hbox2.Add(radio2)
        
#         vbox = wx.BoxSizer(wx.VERTICAL)
#         vbox.Add(hbox1,flg=wx.ALL,border=10)
#         vbox.Add(hbox2,flg=wx.ALL,border=10)

#         #设置面板使用vbox布局管理器
#         panel.SetSizer(vbox)

#         def on_checkbox_click(self,event):
#             cb = event.GetEventObject()
#             print("选择{0}，状态{1}",format(cb,GetLabel(),event.IsChecked()))

#         def on_redio1_click(self,event):
#             rb = event.GetEventObject()
#             print("第一组{0}个被选中",format(rb.GetLabel()))

# app = wx.App()
# frm = MyFrame()
# frm.Show()
# app.MainLoop()
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="复选框和单选按钮", size=(330, 120))
        panel = wx.Panel(parent=self)

        # 创建静态文本和复选框
        st1 = wx.StaticText(panel, label="你最喜欢的编程语言：")
        self.cb1 = wx.CheckBox(panel, id=1, label="Python")
        self.cb2 = wx.CheckBox(panel, id=2, label="Java")
        self.cb2.SetValue(True)  # 默认选中Java
        self.cb3 = wx.CheckBox(panel, id=3, label="C++")
        
        # 绑定复选框事件
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=1)
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=2)
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=3)

        # 创建性别选择的静态文本和单选按钮
        st2 = wx.StaticText(panel, label="选择性别")
        self.rabio1 = wx.RadioButton(panel, id=4, label="男", style=wx.RB_GROUP)
        self.rabio2 = wx.RadioButton(panel, id=5, label="女")

        # 绑定单选按钮事件
        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio_click, id=4)
        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio_click, id=5)

        # 布局管理
        hbox1 = wx.BoxSizer()
        hbox1.Add(st1, flag=wx.LEFT | wx.RIGHT, border=5)
        hbox1.Add(self.cb1)
        hbox1.Add(self.cb2)
        hbox1.Add(self.cb3)

        hbox2 = wx.BoxSizer()
        hbox2.Add(st2, flag=wx.LEFT | wx.RIGHT, border=5)
        hbox2.Add(self.rabio1)
        hbox2.Add(self.rabio2)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1, flag=wx.ALL, border=10)
        vbox.Add(hbox2, flag=wx.ALL, border=10)

        # 设置面板使用vbox布局管理器
        panel.SetSizer(vbox)

    def on_checkbox_click(self, event):
        cb = event.GetEventObject()
        print("选择{0}，状态{1}".format(cb.GetLabel(), event.IsChecked()))

    def on_radio_click(self, event):
        rb = event.GetEventObject()
        print("选中的性别：{0}".format(rb.GetLabel()))

# 运行应用程序
app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()
