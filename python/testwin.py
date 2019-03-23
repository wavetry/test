#!/usr/python
# coding=utf-8
import random

NUM_DIGITS = 3   #全局变量
MAX_GUESS = 10

def getSecretNum():
    # 返回一个由 NUM_DIGITS 个不重复随机数组成的字符串
    numbers = list(range(10))
    random.shuffle(numbers)   #随机修改列表元素的顺序
    secretNum = ''
    for i in range(NUM_DIGITS):   #迭代了NUM_DIGITS次
        secretNum += str(numbers[i])#复合赋值操作
    return secretNum

def getClues(guess,secretNum):
    #返回一个由Pico,Fermi和Bagels 组成的，用来提示用户的字符串
    if guess == secretNum:
        return '恭喜你猜对了！'
    clues =[]
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    clues.sort()   #按照 字母顺序 或 数字顺序重新排列列表中的元素
    return ' '.join(clues)   #组合列表得到字符串

def isOnlyDigits(num):
    #判断玩家输入的是否是一个有效的猜测
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():   #分割字符串返回一个列表，可以简单理解成和join()是逆向过程
            return False
    return True

print('我现在想着一个%s位数字，请试着猜出来！'%(NUM_DIGITS))
print('当我说：|       意思就是：')
print('Bagels  |      没有这个数字')
print('Pico    |       有这个数字但位置错了')
print('Fermi   |       数字存在而且位置也对！')

while True:
    secretNum = getSecretNum()
    print('我接收到一个数字了，你还有 %s 次机会'%(MAX_GUESS))
    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('你猜了 第%s次：'%(guessesTaken))
            guess = input()
        print(getClues(guess,secretNum))
        guessesTaken += 1
        if guess == secretNum:
            break    #如果猜对了，跳出循环
        if guessesTaken > MAX_GUESS:
            print('次数用完了，答案是：%s'%(secretNum))
    print('还想再试一次吗？(yes or no)')
    if not input().lower().startswith('y'):
        break