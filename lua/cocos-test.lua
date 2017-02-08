--
-- Author: Deadline
-- Date: 2016-10-08 14:23:11
--
--闭包
function f1( ... )
	i=0
	local function f2( ... )
		i=i+1
		return i
	end
	i=i+1
	return f2
end

function t1( ... )
	i=0
	i=i+1
	return i
end

-- g1=f1()
-- print(g1()) --2
-- print(g1())
-- print(t1())
-- print(t1())
-- print(i)

--元表
local list = {1,2,3}
local list2 = {4}
local mt = {}
setmetatable(list,mt)
setmetatable(list2,mt)

mt.__index = function ( t,k,v )
	print("__index",t,k,v)
end

-- mt.__newindex = function ( t,k,v )
-- 	print("__newindex",t,k,v)
-- end

mt.__add = function ( t1,t2 )
	for _,item in ipairs(t2)do
		table.insert(t1,item)
	end
	return t1
end

mt.__tostring = function ( ... )
	return "test"
end

function mt.__lt(tA, tB)
    return #tA < #tB
end

-- listsum = list + list2

-- for k,v in ipairs(listsum) do
-- 	print(k,v)
-- end
-- print(list < list2)
local rs = getmetatable(list)
-- for k,v in pairs(rs) do
-- 	print(k,v )
-- 	end
print(list)
