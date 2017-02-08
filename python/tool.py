# from urllib import request

# with request.urlopen("https://www.zhihu.com/question/21669134") as f:
# 	data = f.read()
# 	print("Status",f.status,f.reason)
# 	for k,v in f.getheaders():
# 		print("k,v",k,v)
# 	print("Data:",data.decode('utf-8'))


#!/usr/bin/python
#coding=utf-8

# import urllib
# import re
 
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html.decode('utf-8')

# def getImg(html):
#     reg = r'src="(.+?\.jpg)" pic_ext'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre,html)
#     x = 0
#     print("=========getImg")
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl,'%s.jpg' % x)
#         x+=1
#         print(x)

# html = getHtml("http://tieba.baidu.com/p/3102805968")

# print (getImg(html))



#a text editor
#-*-coding:utf8 -*-  
__version__=0.1 
__author__ ="Alycat" 
 
import sys,tkFileDialog,os  
from Tkinter import *  
 
class Note():  
      
     def __init__(self):  
          self.tk=Tk()  
          self.createUI()  
          self.tk.mainloop()  
 
 
     def createUI(self):  
          #create menu  
          menubar=Menu(self.tk)  
          fmenu=Menu(menubar,tearoff=0)  
          fmenu.add_command(label='Open',command=self.open)  
          fmenu.add_command(label='Save',command=self.save)  
          fmenu.add_command(label='Exit',command=exit)  
          menubar.add_cascade(label="File", menu=fmenu)  
          self.tk.config(menu=menubar)  
          self.text=Text()  
          self.text.pack()  
      
     def save(self):  
        txtContent = self.text.get(1.0,END)  
        self.saveFile(content=txtContent)  
           
 
     def open(self):  
          self.filename = tkFileDialog.askopenfilename(initialdir = os.getcwd())  
          filecontent=self.openFile(fname=self.filename)  
          if filecontent is not -1:  
               self.text.delete(1.0,END)  
               self.text.insert(1.0,filecontent)  
 
     '''''  
          The fname is file name with full path  
     ''' 
     def openFile(self,fname=None):  
          if fname is None:  
               return -1 
          self.fname = fname  
          file = open(fname,'r+')  
          content = file.read()  
          file.close()  
          return content  
 
     def saveFile(self,content=None):  
          if content is None:  
               return -1 
          file=open(self.fname,'w')  
          file.write(content)  
          file.flush()  
          file.close()  
          return 0 
 
     def exit(self):  
          sys.exit(0)  
 
# if __name__ == '__main__':  
#      Note()  










