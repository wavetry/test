import wx 
import sys
sys.path.append('/Users/youai/develop/test/python/pyspider/spider_yupoo.py')
# from spider_yupoo import spider
from pyspider.spider_yupoo import spider
 
class Example(wx.Frame): 
   
   def __init__(self, parent, title): 
      super(Example, self).__init__(parent, title = title, size = (200,200)) 
             
      self.InitUI() 
      self.Centre() 
      self.Show()
		
   def InitUI(self): 
      p = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      l1 = wx.StaticText(p,label = "Enter page number",style = wx.ALIGN_CENTRE ) 
      vbox.Add(l1,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 20) 

      t = wx.TextCtrl(p) 
      vbox.Add(t,1,wx.EXPAND,5) 
      hbox = wx.BoxSizer(wx.HORIZONTAL) 

      b3 = wx.Button(p,label = "Start") 
      hbox.AddStretchSpacer(1) 
      hbox.Add(b3,0,wx.ALIGN_LEFT,20) 
      vbox.Add(hbox,1,wx.ALL|wx.EXPAND) 
      p.SetSizer(vbox) 
          
app = wx.App() 
Example(None, title = 'Scrapy') 
app.MainLoop()