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
