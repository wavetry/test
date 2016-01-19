-- repeat 
--   line = io.read()
-- until line ~= ""
-- print(line)

-- function add( ... )
--   local a,b = ...
--   return a,...
-- end
-- print(add(1,2,3,4,3,4,21)) 

-- function recrusive( ... )
--   print("r",...)
--   recrusive(...)
-- end
-- recrusive(1)

-- function function_name( ... )
--   for i = 1,select('#',...) do
--     print(select(i,...))
--   end
-- end

-- function_name(1,2)

-- do 
--   local printMy = print
--   local k = math.pi / 180
--   print = function (...)
--     return printMy("myInfo",...)
--   end
-- end
-- print(1,23,4)


-- local fact
-- fact = function ( n )
--   if 0 == n then
--     return 1
--   else
--     return fact(n - 1)* n
--   end
-- end
-- print(fact(5))

-- local f,g
-- local function f( ... )
--   print("f",...)
--   g(...)
-- end

-- function g( ... )
--   print("g",...)
--   f(...)
-- end
-- f(1,2,3,4)

-- function foo( n )
--   -- body
--   if n > 1 then 
--     return foo(n - 1) - 1
--   else
--     return 1
--   end
-- end
-- print(foo(10))



function allwords(  )
  local line = io.read()
  local pos = 1
  return function ( )
    while(line )do
      local s,e = string.find(line,"%w+",pos)
      if s then
        pos = e + 1
        return string.sub(line,s ,e)
      else
        line = io.read()
        pos = 1
      end
    end
    return nil
  end
end
-- for word in allwords() do
--   print(word)
-- end
-- function foo( n )
--   assert(n == 0,"n should not be zero "..n)
-- end
-- function er( ... )
--   return "asdasd"
-- end
-- local r,e = xpcall(foo(0))
-- print(r,e)

--协同程序
-- local co = coroutine.create(function (a,c,r )
--   for i = 1,10 do
--     print("co",i,coroutine.yield())
    
--   end
-- end)
-- coroutine.resume(co,a,c,r)
-- coroutine.resume(co)
-- coroutine.resume(co)
-- coroutine.resume(co)
-- coroutine.resume(co)
-- coroutine.resume(co)
-- coroutine.resume(co)
-- coroutine.resume(co)
-- coroutine.resume(co)
-- coroutine.resume(co)
-- print(coroutine.status(co))
-- print(coroutine.resume(co)) 
-- print(coroutine.resume(co)) 

--生产者消费者模型
-- function receive( prod )
--   local status,value = coroutine.resume(prod)
--   print("receive",value)
--   return value
-- end

-- function send( x )
-- print("send",x)
--   coroutine.yield(x)
-- end

-- function producer( )
--   return coroutine.create(function ( )
--     while true do
--       local x = io.read()
--       send(x)
--     end
--   end)
-- end

-- function filter( prod )
--   return coroutine.create(function (  )
--     for line = 1,math.huge do
--       local x = receive(prod)
--       x = string.format("%5d %s",line,x)
--       send(x)
--     end
--   end)
-- end

-- function consumer( prod )
--   while true do
--     local x = receive(prod)
--     io.write(x,"\n")
--   end
-- end
-- p = producer()
-- f = filter(p)
-- consumer(f)
-- coroutine.resume(p)

--图
-- local function name2node(graph,bname )
--   if not graph[bname] then
--     graph[bname] = {name = bname ,adj = {}}
--   end
--   return graph[bname]
-- end

-- function readgraph( )
--   local graph = {}
--   for line in io.lines() do
--     local namefrom,nameto = string.match(line, "(%S+)%s+(%S+)")
--     local from = name2node(graph,namefrom)
--     local to = name2node(graph,nameto)
--     from.adj[to] = true
--   end
--   return graph
-- end

-- function findpath( curr,to,path,visited)
--   path = path or {}
--   visited = visited or {}
--   if visited[curr] then
--     return nil
--   end
--   visited[curr] = true
--   path[#path + 1] = curr
--   if curr == to then
--     return path
--   end

--   for node in pairs(curr.adj) do
--     local p = findpath(node, to, path, visited)
--     if p then return p end
--   end
--   path[#path+1] = nil
-- end

-- function printpath( path )
--   for i = 1,#path do
--     print(path[i].name)
--   end
-- end

-- local g = readgraph()
-- a = name2node(g,"a")
-- b = name2node(g,"b")
-- p = findpath(a, b)
-- if p then printpath(p) end

--序列化
-- function quote( s )
--   local n = -1
--   for w in string.gmatch(s,"]=*") do
--     n = math.max(n,#w - 1)
--   end
--   local eq = string.rep("=",n + 1)
--   return string.format(" [%s[\n%s]%s] ",eq,s,eq)
-- end
-- print(quote("]]==my name is linzhilang=[["))

-- function serialize(o)
--   -- body
--   if type(o) == "number" then
--     io.write(o)
--   elseif type(o) == "string" then
--     io.write(string.format("%q",o))
--   elseif type(o) == "table" then
--     io.write(" {\n ")
--     for k,v in pairs(o) do
--       io.write("  ",k," = ")
--       serialize(v)
--       io.write(",\n")

--     end
--     io.write("}\n")
--   else
--     error("can not serialize a "..type(o))

--   end
-- end

-- serialize({a = 1,b = {[1] = 5}})
local a = io.read()
print(a)