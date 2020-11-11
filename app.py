from pyautogui import *
import pyautogui
import keyboard
import win32api, win32con
import time

# (541,468) (628,468) (714,468) (823,468) Position of tiles to be pressed


def click_tile(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('space')==False:
    
    if pyautogui.pixel(541,468)==(0,0,0):
        click_tile(541,468)
    
    if pyautogui.pixel(628,468)==(0,0,0):
        click_tile(628,468)
    
    if pyautogui.pixel(714,468)==(0,0,0):
        click_tile(714,468)
    
    if pyautogui.pixel(823,468)==(0,0,0):
        click_tile(823,468)

 
