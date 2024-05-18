# #getting python to type the number
from pynput.keyboard import Key,Controller
keyboard= Controller()
import pyautogui as pg

pg.moveTo(1370,430,2)
pg.click(1370,430)
keyboard.type((str(num)))

# getting it to press sumbit

pg.moveTo(1385,568)