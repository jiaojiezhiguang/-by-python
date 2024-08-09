# import wx

# #自定义窗口类MyFrame
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(None,title="Please caowo",size=(400,300),pos=(100,100))
#         panel = wx.Panel(parent = self)
#         self.statictext = wx.StaticText(parent=panel,label="Hello World!",pos=(150,120))
#         # b = wx.Button(parent=panel,label="ok",pos=(150,170))
#         b1 = wx.Button(parent=panel,id=10,label="Button1")
#         b2 = wx.Button(parent=panel,id=11,label="Button2")
#         #创建水平方向的盒子布局管理器hbox对象
#         hbox = wx.BoxSizer(wx.HORIZONTAL)
#         #添加b1到hbox布局管理
#         hbox.Add(b1,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)
#         hbox.Add(b2,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)
#         #创建垂直方向的盒子布局管理器对象vbox
#         vbox = wx.BoxSizer(wx.VERTICAL)
#         #添加静态文本到vbox布局管理器
#         vbox.Add(self.statictext,proportion=1,
#             flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.TOP,border=30)
#         #添加hbox到vbox布局管理器
#         # vbox.Add(b,proportion=1,flag=wx.EXPAND|wx.BOTTOM,border=10)
#         vbox.Add(hbox,proportion=1,flag=wx.CENTER)
#         #设置面板panel采用vbox布局管理器
#         panel.SetSizer(vbox)
#         self.Bind(wx.EVT_BUTTON,self.on_click,id=10,id2=20)
    
#     def on_click(self,event):
#         # self.statictext.SetLabelText("Hello")
#         event_id = event.Getid()
#         print(event_id)
#         if event_id == 10:
#             self.statictext.SetLabel("Button1单")
#         self.statictext.SetLabel("Button2但")

# #创建应用程序对象
# app = wx.App() 
# #创建窗口对象
# frm = MyFrame()
# #显示窗口
# frm.Show()
# #进入主事件循环
# app.MainLoop()
import wx

# 自定义窗口类 MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Please caowo", size=(400, 300), pos=(100, 100))
        
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel, label="Hello World!", pos=(150, 120))
        
        # 创建两个按钮
        b1 = wx.Button(parent=panel, id=10, label="Button1")
        b2 = wx.Button(parent=panel, id=11, label="Button2")
        
        # 创建水平方向的盒子布局管理器 hbox
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # 添加 b1 和 b2 到 hbox 布局管理器
        hbox.Add(b1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hbox.Add(b2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        
        # 创建垂直方向的盒子布局管理器对象 vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 添加静态文本到 vbox 布局管理器
        vbox.Add(self.statictext, proportion=2,
                 flag=wx.ALIGN_CENTER_HORIZONTAL | wx.FIXED_MINSIZE | wx.TOP, border=30)
        # 添加 hbox 到 vbox 布局管理器
        vbox.Add(hbox, proportion=1, flag=wx.CENTER)
        
        # 设置面板 panel 采用 vbox 布局管理器
        panel.SetSizer(vbox)
        
        # 绑定按钮点击事件
        b1.Bind(wx.EVT_BUTTON, self.on_click)
        b2.Bind(wx.EVT_BUTTON, self.on_click)
    
    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabel("Button1 clicked")
        elif event_id == 11:
            self.statictext.SetLabel("Button2 clicked")

# 创建应用程序对象
app = wx.App() 
# 创建窗口对象
frm = MyFrame()
# 显示窗口
frm.Show()
# 进入主事件循环
app.MainLoop()
