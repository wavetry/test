# def get_a_down_arrow_of(n):
#         temp = n
#         result = []
#         while n > 0:
#                 line = ''
#                 spaces = ''
#                 for i in range(1,n+1):
#                         line = line + str(i%10)
#                 reverse = line[0:-1]
#                 n = n - 1
#                 for j in range(temp - n - 1):
#                         spaces = spaces + ' '
#                 result.append(spaces + line+reverse[::-1])
#         return '\n'.join(result)


# def half(i,n):
#         return "".join(str(d%10)for d in range(1,n-i+1))
# def line(i,n):
#         h = half(i,n)
#         return " " * i + h + h[-2::-1]
# def get_a_down_arrow_of(n):
#         return "\n".join(line(i,n) for i in range(n))
# insert = input('number:')
# print(get_a_down_arrow_of(insert))

#############
# def is_palindromic(val):
#         val = str(val)
#         return val == val[::-1]

# def next_pal(val):
#         while True:
#                 val = val + 1
#                 if is_palindromic(val):
#                         return val
                
# insert = input('number:')
# print(next_pal(insert))
#################

# def match_arrays(v,r):
#         vset = set(v)
#         rset = set(r)
#         return len(vset & rset)
# import pickle

# def match_arrays(v,r):
#         dic = {}
#         total = 0
#         for i in v:
#                 dic[pickle.dumps(i)] = True

#         for j in r:
#                 if pickle.dumps(j) in dic:
#                         total += 1
#         return total
# print(match_arrays(['Perl','Closure','JavaScript',[1,2]],['Go', 'C++','JavaScript']))

# def match_arrays(v, r):
#     return sum(1 for x in v if x in r)
# import math
# def is_square(n):
#         if n < 0:
#                 return False
#         nsqrt = math.sqrt(n)
#         result = math.modf(nsqrt)
#         return result[0] == 0
# def is_square(n):
#   return n ** .5 % 1 == 0 if n > 0 else False
# insert = input('number')
# print(is_square(insert))

def min_max(lst):
        lst = sorted(lst)
        return [lst[0],lst[-1]]

def make_lazy(*args):
        return lambda : args[0](*args[1:])

# from functools import partial as make_lazy
                
        
def modding(a,b):
    return a%b

class HTMLGen(object):
    def __getattr__(self, name):
        def wrapper(text):
            if name == "comment":
                return "<!--{0}-->".format(text)
            else:
                return "<{0}>{1}</{0}>".format(name, text)
        return wrapper

def my_parse_int(string):
       try:
               return int(string)
       except ValueError:
               return "NaN"
#(123) 456-7890
import re
def validPhoneNumber(phoneNumber):
        if re.match(r'^\(\d{3}\) \d{3}\-\d{4}$',phoneNumber):
                return True
        else:
                return False


def multiplication_table(row,col):
        result = []
        for i in range(1,row+1):
                temp = []
                for j in range(0,col):
                        temp.append((j+1)*i)
                result.append(temp)
        return result

def multiplication_table(row,col):
    return [[x*y for y in range(1,col+1)] for x in range(1,row+1)]


def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
# print duplicate_encode('din')


def tribonacci(signature,n):
        result = signature
        while len(result) < n:
                result.append(signature[-1]+signature[-2]+signature[-3])
        return result
# print tribonacci([1,1,1],10)

from random import randint,seed
seed(1)
guess = randint(1,100)
seed(1)

# greddy alorithem
def knapsack(capacity,items):
    value_per_weight = []
    result = []
    k = 0
    for item in items :
        value_per_weight.append((k,float(item[1])/item[0]))
        k += 1
    value_per_weight.sort(lambda x,y:cmp(x[1],y[1]),reverse=True)
    print(value_per_weight)
    for item in value_per_weight:
        result.insert(item[0],capacity/item[1])
        capacity = capacity % item[1]
        if capacity == 0:
            break
    return result
print(knapsack(100,((60,80),(50,50)))) 

def group_check(s):
    while "{}" in s or "()" in s or "[]" in s:
        s = s.replace("{}","").replace("()","").replace("[]","")
    return not s

print(group_check("({"))






        














