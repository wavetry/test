#!/usr/python3
# coding=utf-8

import lupa,os,sys
from lupa import LuaRuntime
lua = LuaRuntime(unpack_returned_tuples=True)

luaclone = '''
function clone(object)
    local lookup_table = {}
    local function _copy(object)
        if type(object) ~= "table" then
            return object
        elseif lookup_table[object] then
            return lookup_table[object]
        end
        local new_table = {}
        lookup_table[object] = new_table
        for key, value in pairs(object) do
            new_table[_copy(key)] = _copy(value)
        end
        return setmetatable(new_table, getmetatable(object))
    end
    return _copy(object)
end

'''
def checklua(path):
	try:
		file_name = os.path.basename(path).split('.')[0]
		with open(path,'r',encoding="UTF-8") as f:
			content = f.read()
			lua.execute(luaclone + content)
			g = lua.globals()
			if file_name == "CommonConfig":
				channel = input("检测CommonConfig需要输入渠道：")
				CommonConfig = g.CommonConfig
				return CommonConfig[100000].value[1][1] == channel
			elif file_name == "ChannelConfig":
				channel = input("检测ChannelConfig需要输入渠道：")
				ChannelConfig = g.ChannelConfig
				for value in ChannelConfig.values():
					return channel == value.name
			else:
				return True
	except Exception as e:
		return False

if __name__ == "__main__":
	argv = sys.argv
	file_list = argv[1:]
	
	if len(file_list) > 0:
		for file_name in file_list:
			file_ext = os.path.splitext(file_name)[1]
			if file_ext == ".lua":
				if checklua(file_name):
					print("文件检测通过%s" % file_name)
				else:
					print("【【【文件检测不通过】】】 %s" % file_name)
	else:
		print("没有传入文件")
	os.system("pause")