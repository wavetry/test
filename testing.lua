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


--输入字符窜反转
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
-- end

-- reverse( input )
-- print(math.ldexp(1,16))



