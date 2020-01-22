### Trial verison of tessaract
### first pip install tessaract
### download tessaract.exe from https://github.com/tesseract-ocr/tesseract/wiki
### pip install opencv-python
from PIL import Image
import pytesseract
import numpy as np
import cv2
import sys
from io import BytesIO
from PIL import Image

def refine(image: Image):
    def restructure(res):
        return np.ones(res, np.uint8)
    i_arr = np.asarray(image)
    _, threshold = cv2.threshold(i_arr, 200, 255, cv2.THRESH_BINARY)
    inv = cv2.bitwise_not(threshold)
    m_Large = cv2.resize(inv, (0,0), fx=2, fy=2)
    p_1 = cv2.erode(m_Large, restructure([3,3]), iterations=2)
    p_2 = cv2.dilate(p_1, restructure([2,2]), iterations=1)
    smolagn = cv2.resize(p_2,(0,0),fx = 0.5, fy =0.5)
    return Image.fromarray(smolagn)

url = input("input URL and name of your image: ")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
image = Image.open(url)
text = pytesseract.image_to_string(image)
if not text:
    image = refine(image)
    image = refine(image)
    text = pytesseract.image_to_string(image)

image.save("refinedImage.jpg")
print(text)

