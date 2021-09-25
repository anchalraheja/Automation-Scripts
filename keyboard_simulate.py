from pyautogui import press, typewrite, hotkey
import time 
FAILSAFE = True

time.sleep(1.5)    

for x in range(1,5000):
	time.sleep(10)
	y = str(x)
	typewrite(y)    
	hotkey('enter')