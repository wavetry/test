import itchat 
import time
itchat.auto_login(hotReload=True)
name = input("name:")
message=input("message:")
print(itchat.search_friends(remarkName=name))
boom_obj = itchat.search_friends(remarkName=name)[0]['UserName']
for i in range(10):
	time.sleep(0.5)
	itchat.send_msg(msg=message,toUserName=boom_obj)