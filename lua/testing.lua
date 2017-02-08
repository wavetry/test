-- 打印乘法表
-- local result = {}
-- for i = 1,10 do
-- 	result[i] = {}
-- 	for j = 1,i do
-- 		local s = i .." x ".. j .. "=".. i * j
-- 		result[i][j] = s
-- 	end
-- end
-- local final = {}
-- for i = 1,#result do
-- 	final[i] = ""
-- 	for j = 1,#result[i] do
-- 		final[i] = final[i]..result[i][j].."   "
-- 		-- print(result[i][j])
-- 	end
-- end

-- for i = 1,#final do
-- 	print(final[i])
-- end

--求PI
-- print("input a number:")
-- local pi = 0
-- local input = tonumber(io.read()) + 1
-- for i = 1 ,input  do
-- 	if i%2 == 1 then
-- 		pi = pi + (4/(2*i - 1))
-- 	else
-- 		pi = pi - (4/(2*i - 1))
-- 	end
-- end
-- print("pi====",pi)

--求质数
-- local prime
-- local input = tonumber(io.read()) 
-- for i = 2,input do
-- 	prime = true
-- 	for j = 2,10 do
-- 		if (i%j == 0) and i ~= j then
-- 			prime = false
-- 		end
-- 	end
-- 	if prime then
-- 		print("====",i)
-- 	end
-- end

--检查邮件地址合法与否
-- local nextchar
-- local gotAt 
-- local gotDot
-- print("insert you email address")
-- nextchar = io.read()


-- while (nextchar  ~= ' ' and nextchar  ~= "\n") do
-- 	if nextchar == '@' then
-- 		gotAt = true
-- 	else
-- 		gotAt = false
-- 	end
-- 	if nextchar == '.' and gotAt then
-- 		gotDot = true
-- 	end
-- 	nextchar = io.read()
-- end
-- if gotAt and gotDot then
-- 	print("valid address")
-- else
-- 	print("wrong")
-- end

-- local file = io.open("logic.lua","a+")
-- -- file:close()

-- file:write("\"===================== my name is linzhilang\"\n")

-- file:flush()
-- file:close()
-- for line in file:lines() do
-- 	print(line)
-- end


-- --输入字符窜反转
-- nextchar = io.read()
-- local input = {}
-- local i = 1
-- while nextchar~=' ' and nextchar ~= '\n' do
-- 	if string.len(nextchar) > 1 then
-- 		print("too long ")
-- 	elseif string.len(nextchar) == 0 then
-- 		print("too short")
-- 	else
-- 		input[i] = nextchar
-- 		i = i + 1
-- 	end
-- 	nextchar = io.read()
-- end

-- function reverse( input )
-- 	local times = math.floor(#input/2)
-- 	local temp
-- 	for i=times,1,-1 do
-- 		temp = input[i]
-- 		input[i] = input[#input-i+1]
-- 		input[#input-i+1] = temp
-- 	end
-- 	print(table.concat(input,''))
-- end

-- reverse( input )
-- print(math.ldexp(1,16))

-- --bubble sort
-- function bubble( t,check )
-- 	-- assets(type(check) == "function","check must be a function")
-- 	for i = 1,#t do
-- 		for j = i+1,#t do
-- 			if check(t[i],t[j]) then
-- 				local temp = t[i]
-- 				t[i] = t[j]
-- 				t[j]= temp
-- 			end
-- 		end
-- 	end
-- end

-- local list = {1,-1,100,1,0,-9}
-- local function check( a,b )
-- 	return a > b
-- end
-- bubble(list,check)


-- function partition( list,low,high )
-- 	-- body
-- end



-- local sortList = {1,5,6,21,3,4,3,6,23,4,3,6,2,3,4,6234,234}

-- function partion( array,low,high)
-- 	local key = array[low]
-- 	local index = low
	
-- 	array[index],array[high] = array[high],array[index]
-- 	local i = low
-- 	while i < high do
-- 		if key > array[i] then
-- 			array[index],array[i] = array[i],array[index]
-- 			index = index + 1
-- 		end
-- 		i = i + 1
-- 	end
-- 	array[high],array[index] = array[index],array[high]
-- 	return index
-- end

-- function quick( array ,low , high)
-- 	if low < high then
-- 		local index = partion(array,low,high)
-- 		quick(array,low,index - 1)
-- 		quick(array,index+1,high)
-- 	end
-- end

-- local function quickSort( array )
-- 	quick(array,1,#array)
-- end

-- quickSort(sortList)

-- for k,v in ipairs(sortList) do
-- 	print(k,v)
-- end

-- --closure 闭包
-- function test( )
-- 	local i = 0
-- 	return function ( ... )
-- 		i = i + 1
-- 		return i
-- 	end
-- end

-- local t1 = test()
-- local t2 = test()
-- print(t1())
-- print(t1())
-- print(t2())
-- print(t2())
-- t1 = test()
-- print(t1())

--闭包构建迭代器
-- function list_iter( t )
-- 	local i = 0 
-- 	local n = #t
-- 	return function ( ... )
-- 		i = i + 1
-- 		if i <= n then return t[i] end
-- 	end
-- end

-- t = {1,2,3}
-- local iter = list_iter(t)
-- while true do
-- 	local ele = iter()
-- 	if ele == nil then break end
-- 	print(ele)
-- end

-- for ele in list_iter(t) do
-- 	print(ele)
-- end

--datastructure by lua
List = {}
function List.new( ... )
	return {first = 0,last = -1}
end

function List.pushFront(list,value )
	list.first = list.first - 1
	list[list.first]=value
end

function List.pushBack( list,value )
	list.last = list.last + 1
	list[list.last] = value
end

function List.popFront( list )
	local first = list.first
	if first > list.last then error("List id empty!") end
	local value = list[first]
	list[first] = nil
	list.first = first + 1
	return value
end

function List.popBack( list )
	local last = list.last
	if last < list.first then
		error("table is empty!")
	end
	local value = list[last]
	list[last] = nil
	list.last = list.last - 1
	return value
end

-- local list = List.new()
-- List.pushFront(list,1)
-- List.pushFront(list,2)
-- List.pushBack(list,3)
-- for k,v in pairs(list) do
-- 	print(k,v)
-- 	end
-- print(List.popFront(list))
-- print(List.popBack(list))

-- local t = {}
-- for line in io.lines() do
-- 	if line == nil  then break end
-- 	t[#t+1] = line
-- end
-- local s = table.concat(t,"\n")
-- print(s)

-- continue
-- for i = 1,100 do
-- 	while true do
-- 		if i % 2 == 1 then break end
-- 		print(i)
-- 		break
-- 	end
-- end

-- for i = 1,100 do
-- 	repeat
-- 		if i % 2 == 1 then break end
-- 		print(i)
-- 	until true
-- end

--weak table
-- local a = {}
-- b = {__mode = "k"}
-- setmetatable(a,b)
-- key = {}
-- a[key] = 1
-- key = {}
-- a[key] = 2
-- collectgarbage()
-- for k,v in pairs(a) do
-- 	print(k,v)
-- end

-- local t = {1,2,3}
-- t[2] = nil

-- for i = 1 ,#t do
-- 	t[i] = nil
-- 	-- table.remove(t,i)
-- end

-- for k, v in pairs(t) do
-- 	print(k,v)
-- end

-- 钩子函数
local Counters = {}
local Names = {}
local function hook( ... )
	local f = debug.getinfo(2,"f").func
	if Counters[f] == nil then
		Counters[f] = 1
		Names[f] = debug.getinfo(2,"Sn")
	else
		Counters[f] = Counters[f] + 1
	end
end

function getname( func )
	local n = Names[func]
	if n.what == "C" then
		return n.name
	end
	local lc = string.format("[%s]:%s",n.short_src,n.linedefined)
	if n.namewhat ~= "" then
		return string.format("%s (%s)",lc,n.name)
	else
		return lc 
	end
end

local f = assert(loadfile(arg[1]))
debug.sethook(hook,"c")
f()
debug.sethook()

for func ,count in pairs(Counters) do
	print(getname(func),count)
end

-- local sin = math.sin
-- function foo (x)
--     for i = 1, 1000000 do
--         x = x + sin(i)
--     end
--     return x
-- end

-- print(foo(10))