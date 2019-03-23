#!/usr/python
# coding=utf-8
import time
import autopy
import win32api
import win32con
# autopy.mouse.smooth_move(1,1)
# autopy.mouse.move(1,1)


win32api.keybd_event(18,0,0,0)
win32api.keybd_event(9,0,0,0)
time.sleep(0.5)
win32api.keybd_event(13,0,0,0)
win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
time.sleep(2)
