--
-- Author: Deadline
-- Date: 2016-10-13 15:01:36
--
--二分查找
function binarySearch( array,key)
	local low = 1
	local high = #array
	while low <= high do
		print(low,high)
		local mid = math.floor((low + high) / 2)
		if key > array[mid] then
			low = mid
		elseif key < array[mid] then
			high = mid
		else
			return mid
		end
	end
	return -1
end

-- local a = {1,3,5,6,7,8,9,12,34}
-- local key = tonumber(io.read())
-- print(binarySearch(a,key))


local function printA( array )
	for i =  1,#array do
		print(array[i])
	end
end

--选择排序
local selectSort = function ( array )
	for i = 1,#array do
		local min = i
		for j = i,#array do
			if array[j] < array[min] then
				min = j
			end
		end
		array[i],array[min] = array[min],array[i]
	end
end

--插入排序
local function insertSort( array )
	for i = 1,#array do
		for j = i,#array do
			if array[j] < array[i] then
				array[i],array[j] = array[j],array[i]
			end
		end
	end
end

--冒泡
local function bubbleSort( array )
	for i = 1,#array do
		for j = #array,i+1,-1 do
			if array[j] < array[j-1] then
				array[j],array[j-1] = array[j-1],array[j]
			end
		end
	end
end

local function partion(array,low,high) 
	local key = array[low]
	local index= low
	local i = low
	array[index],array[high] = array[high],array[index]
	while i < high do
		if key > array[i] then
			array[index],array[i] = array[i],array[index]
			index = index + 1
		end
		i = i+1
	end
	array[high],array[index] = array[index],array[high]
	return index
end

local function quickSort(array,low,high  )
	if low < high then
		local partion = partion(array,low,high)
		quickSort(array,low,partion - 1)
		quickSort(array,partion+1,high)
	end
end

local function quickSort1( array,low,high )
	if low < high then
		local i = low
		local j = high
		local key = array[i]
		while i < j do
			while (i < j and array[j] >= key ) do
				j = j - 1
			end
			if i < j then
				i = i + 1
				array[i] = array[j]
			end

			while(i < j and array[i] < key ) do
				i = i + 1
			end

			if i < j then
				j = j - 1
				array[j] = array[i]
			end

		end
		array[i] = key
		quickSort1(array,low,i - 1)
		quickSort1(array,i + 1,high)
	end

end

local test = {1,23,5,6,2,34,62,34,6,23,6,2,4,6}
quickSort1(test,1,#test)
printA(test)



