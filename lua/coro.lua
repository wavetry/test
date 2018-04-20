--
-- Author: Deadline
-- Date: 2017-09-05 10:16:33
--
coro = {}
coro.main = function() end

coro.current = coro.main
function coro.create( f )
	return coroutine.wrap(function ( val )
		return nil,f(val)
	end)
end

function coro.transfer(k,val)
	if coro.current ~= coro.main then
		return coroutine.yield(k,val)
	else
		while k do
			coro.current = k
			if k == coro.main then
				return val
			end
			k,val = k(val)
		end
		error("coroutine ended without transfering control...")
	end
end