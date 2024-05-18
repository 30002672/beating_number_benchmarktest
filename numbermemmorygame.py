
# take a picture of screen

# narrow screen to only see numbers

# output the numbers which it sees with picture

#https://humanbenchmark.com/tests/number-memory

import pyautogui as pg

print(pg.size())
print(pg.position())
pg.moveTo(1385,568,1)
pg.click(1385,568)

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



#code which interprets numbers from image
from PIL import Image
import pytesseract

path = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#image_path = r'C:\Users\Owner\Pictures\Screenshots\number.png.png'
image_path = "C:\\Users\\Owner\\Pictures\\Saved Pictures\\result.png"

img = Image.open(image_path)

pytesseract.pytesseract.tesseract_cmd = path
text = pytesseract.image_to_string(img,lang='eng', config='--psm 6')
num = (text[:-1])
print(num)

#
# #getting python to type the number
from pynput.keyboard import Key,Controller
keyboard= Controller()
import pyautogui as pg

pg.moveTo(1370,430,2)
pg.click(1370,430)
keyboard.type((str(num)))

# getting it to press sumbit

pg.moveTo(1385,568)
#pg.click(1385,568)

#keyboard.release('p')