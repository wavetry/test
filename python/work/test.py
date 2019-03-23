# from operator import itemgetter, attrgetter
# test = [(1,"1"),(3,"3"),(2,"2")]
# test.sort(key=lambda obj:obj[0])
# print(test)
import re
test = "--print("
cnpattern4 = re.compile(u'--[.]*')
print cnpattern4.search(test)