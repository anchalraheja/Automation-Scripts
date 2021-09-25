from pyautogui import press, typewrite, hotkey
import pyautogui
import time 
FAILSAFE = True

time.sleep(2)    

for x in range(0,300):
	pyautogui.moveTo(308,1005) #adjust your chat box
	pyautogui.click()
	hotkey('up')
	hotkey('command', 'a')
	hotkey('del')
	hotkey('enter')
	hotkey('enter')
	print x