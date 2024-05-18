# code which takes a screenshot
import pygetwindow
import pyautogui
from PIL import Image

path = "C:\\Users\\Owner\\Pictures\\Saved Pictures\\result.png"
titles = pyautogui.getAllTitles()

window = pygetwindow.getWindowsWithTitle('Human Benchmark - Number Memory Test - Google Chrome')[0]

left,top = window.topleft
right, bottom = window.bottomright
pyautogui.screenshot(path)
im = Image.open(path)
im = im.crop((left+10,top+200,right-50,bottom-650))
im.save(path)
#im.show(path)
