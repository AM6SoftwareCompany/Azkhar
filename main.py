import time
import webbrowser

import pyautogui

webbrowser.open_new('https://business.facebook.com/creatorstudio/home')
time.sleep(10)
pyautogui.moveTo(950, 300, duration=1)
pyautogui.click()
pyautogui.PAUSE = 5
pyautogui.moveTo(900, 200, duration=1)
pyautogui.click()
pyautogui.write('apocryphon')
pyautogui.moveTo(970, 270, duration=1)
pyautogui.click()
pyautogui.moveTo(1000, 500, duration=1)
pyautogui.click()
pyautogui.moveTo(150, 400, duration=1)
pyautogui.click()
pyautogui.write('Bot Test1!')
pyautogui.moveTo(250, 700, duration=1)
pyautogui.click()