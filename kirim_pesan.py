# pywhatkit merupakan library python yang digunakan untuk mengirim pesan ke whatshap
# flask merupakan web server yang digunakan oleh pyhon
# pyautogui merupakan library dari python untuk kontrol moute dan type dari sistem

import pywhatkit 
import pyautogui
import time

pywhatkit.sendwhatmsg("+6285238661660","halo saya ular", 23,12)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.press("enter")
