# -*- coding: utf-8 -*-
# import wx 
# import sys
# sys.path.append('/Users/youai/develop/test/python/pyspider/spider_yupoo.py')
# # from spider_yupoo import spider
# from spider_yupoo import spider
 
# class Example(wx.Frame): 
   
#    def __init__(self, parent, title): 
#       super(Example, self).__init__(parent, title = title, size = (200,200)) 
             
#       self.InitUI() 
#       self.Centre() 
#       self.Show()
		
#    def InitUI(self): 
#       p = wx.Panel(self) 
#       vbox = wx.BoxSizer(wx.VERTICAL) 
#       l1 = wx.StaticText(p,label = "Enter page number",style = wx.ALIGN_CENTRE ) 
#       vbox.Add(l1,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 20) 

#       t = wx.TextCtrl(p) 
#       vbox.Add(t,1,wx.EXPAND,5) 
#       hbox = wx.BoxSizer(wx.HORIZONTAL) 

#       b3 = wx.Button(p,label = "Start") 
#       hbox.AddStretchSpacer(1) 
#       hbox.Add(b3,0,wx.ALIGN_LEFT,20) 
#       vbox.Add(hbox,1,wx.ALL|wx.EXPAND) 
#       p.SetSizer(vbox) 
          
# app = wx.App() 
# Example(None, title = 'Scrapy') 
# app.MainLoop()


# import wx 
 
# class MDIFrame(wx.MDIParentFrame): 
#    def __init__(self): 
#       wx.MDIParentFrame.__init__(self, None, -1, "MDI Parent - www.yiibai.com", size = (600,400)) 
#       menu = wx.Menu() 
#       menu.Append(5000, "&New Window") 
#       menu.Append(5001, "&Exit") 
#       menubar = wx.MenuBar() 
#       menubar.Append(menu, "&File") 
      
#       self.SetMenuBar(menubar) 
#       self.Bind(wx.EVT_MENU, self.OnNewWindow, id = 5000) 
#       self.Bind(wx.EVT_MENU, self.OnExit, id = 5001) 
      
#    def OnExit(self, evt): 
#       self.Close(True)  
      
#    def OnNewWindow(self, evt): 
#       win = wx.MDIChildFrame(self, -1, "Child Window")
#       win.Show(True) 
      
# app = wx.App() 
# frame = MDIFrame() 
# frame.Show() 
# app.MainLoop()


# import wx 
 
# class Mywin(wx.Frame): 
            
#    def __init__(self, parent, title): 
#       super(Mywin, self).__init__(parent, title = title,size = (500,300))  
#       self.InitUI() 
         
#    def InitUI(self): 
#       self.Bind(wx.EVT_PAINT, self.OnPaint) 
#       self.Centre() 
#       self.Show(True)
      
#    def OnPaint(self, e): 
#       dc = wx.PaintDC(self) 
#       brush = wx.Brush("white")  
#       dc.SetBackground(brush)  
#       dc.Clear() 
        
#       dc.DrawBitmap(wx.Bitmap("test.jpg"),10,10,True) 
#       color = wx.Colour(255,0,0)
#       b = wx.Brush(color) 
      
#       dc.SetBrush(b) 
#       dc.DrawCircle(300,125,50) 
#       dc.SetBrush(wx.Brush(wx.Colour(255,255,255))) 
#       dc.DrawCircle(300,125,30) 
      
#       font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
#       dc.SetFont(font) 
#       dc.DrawText("Hello wxPython",200,10) 
      
#       pen = wx.Pen(wx.Colour(0,0,255)) 
#       dc.SetPen(pen) 
#       dc.DrawLine(200,50,350,50) 
#       dc.SetBrush(wx.Brush(wx.Colour(0,255,0), wx.CROSS_HATCH)) 
#       dc.DrawRectangle(380, 15, 90, 60) 
      
# ex = wx.App() 
# Mywin(None,'Drawing Demo - www.yiibai.com') 
# ex.MainLoop()

#！-coding = utf8 #
# import wx
# from spider_yupoo import spider
import spider_yupoo
class Mywin(wx.Frame): 
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (350,100))
      
      panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
         
      hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
      l1 = wx.StaticText(panel, -1, "开始页数：") 
      
      hbox1.Add(l1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      self.t1 = wx.TextCtrl(panel,value = '') 
      
      hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      # self.t1.Bind(wx.EVT_TEXT,self.OnKeyTyped) 
      vbox.Add(hbox1) 
      
      # hbox2 = wx.BoxSizer(wx.HORIZONTAL)
      # l2 = wx.StaticText(panel, -1, "密码文本") 
      
      # hbox2.Add(l2, 1, wx.ALIGN_LEFT|wx.ALL,5) 
      # self.t2 = wx.TextCtrl(panel,style = wx.TE_PASSWORD) 
      # self.t2.SetMaxLength(5) 
      
      # hbox2.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      # vbox.Add(hbox2) 
      # self.t2.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)
      
      # hbox3 = wx.BoxSizer(wx.HORIZONTAL) 
      # l3 = wx.StaticText(panel, -1, "多行文本") 
      
      # hbox3.Add(l3,1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      # self.t3 = wx.TextCtrl(panel,size = (200,100),style = wx.TE_MULTILINE) 
      
      # hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      # vbox.Add(hbox3) 
      # self.t3.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressed)  
      
      hbox4 = wx.BoxSizer(wx.HORIZONTAL) 
      # l4 = wx.StaticText(panel, -1, "只读取文本") 
      # self.l4 = l4
      
      # hbox4.Add(l4, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      # self.t4 = wx.TextCtrl(panel, value = "只读文本",style = wx.TE_READONLY|wx.TE_CENTER) 
         
      # hbox4.Add(self.t4,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      # vbox.Add(hbox4) GetLineText

      b3 = wx.Button(panel,label = "Start") 
      b3.Bind(wx.EVT_BUTTON,self.OnClicked) 
      hbox4.AddStretchSpacer(1) 
      hbox4.Add(b3,0,wx.ALIGN_LEFT,20) 
      vbox.Add(hbox4,1,wx.ALL|wx.EXPAND) 

      panel.SetSizer(vbox) 
        
      self.Centre() 
      self.Show() 
      self.Fit()  
      
   # def OnKeyTyped(self, event): 
   #    print event.GetString() 
      
   # def OnEnterPressed(self,event): 
   #    print "Enter pressed" 
      
   # def OnMaxLen(self,event): 
   #    print "Maximum length reached" 
   def OnClicked(self,event):
      print (self.t1.GetLineText(0))
      
app = wx.App() 
Mywin(None,  'TextCtrl实例-www.yiibai.com')
app.MainLoop()