# -*- coding=utf-8 -*-
import time,sys
from Tools import Tool
#获取当前时间
def getCurrentTime(self):
    return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))
    
#获取当前时间
def getCurrentDate(self):
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))
    
#插入数据
def insertData(self, table, my_dict):
     try:
         self.db.set_character_set('utf8')
         cols = ', '.join(my_dict.keys())
         values = '"," '.join(my_dict.values())
         sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, '"'+values+'"')
         try:
             result = self.cur.execute(sql)
             insert_id = self.db.insert_id()
             self.db.commit()
             #判断是否执行成功
             if result:
                 return insert_id
             else:
                 return 0
         except MySQLdb.Error,e:
             #发生错误时回滚
             self.db.rollback()
             #主键唯一，无法插入
             if "key 'PRIMARY'" in e.args[1]:
                 print self.getCurrentTime(),"数据已存在，未插入数据"
             else:
                 print self.getCurrentTime(),"插入数据失败，原因 %d: %s" % (e.args[0], e.args[1])
     except MySQLdb.Error,e:
         print self.getCurrentTime(),"数据库错误，原因%d: %s" % (e.args[0], e.args[1])

f_handler=open('out.log', 'w') 
sys.stdout=f_handler

#主函数
def main(self):
    f_handler=open('out.log', 'w') 
    sys.stdout=f_handler
    page = open('page.txt', 'r')
    content = page.readline()
    start_page = int(content.strip()) - 1
    page.close()     
    print self.getCurrentTime(),"开始页码",start_page
    print self.getCurrentTime(),"爬虫正在启动,开始爬取爱问知识人问题"
    self.total_num = self.getTotalPageNum()
    print self.getCurrentTime(),"获取到目录页面个数",self.total_num,"个"
    if not start_page:
        start_page = self.total_num
    for x in range(1,start_page):
        print self.getCurrentTime(),"正在抓取第",start_page-x+1,"个页面"
        try:
            self.getQuestions(start_page-x+1)
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print self.getCurrentTime(),"某总页面内抓取或提取失败,错误原因", e.reason
        except Exception,e:  
            print self.getCurrentTime(),"某总页面内抓取或提取失败,错误原因:",e
        if start_page-x+1 < start_page:
            f=open('page.txt','w')
            f.write(str(start_page-x+1))
            print self.getCurrentTime(),"写入新页码",start_page-x+1
            f.close()
