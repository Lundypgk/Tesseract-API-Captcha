# Tesseract-API-Captcha
[PyTesseract](https://github.com/tesseract-ocr/tesseract) is an open source OCR engine that reads images and translates them into text. However usage for Tesseract is limited with regards to CAPTCHA. This is my attempt at solving captcha by manipulating the image with openCV through the usage of dilation and thresholding.

## Effectiveness of program
Currently the program is not full proof and it is effective to a certain extend. For certain situations as documented below dilation and thresholding needs to be applied before tesseract is able to read the image. However for some situations, the image could not be read even with the image being refined
### Stage 1 : Works without CV2
<img src="https://github.com/Lundypgk/Tesseract-API-Captcha/blob/master/testing/captcha1.JPG" alt="Image of first captcha text" width="200" height="auto"><img src="https://github.com/Lundypgk/Tesseract-API-Captcha/blob/master/testing/Kenobi.jpg" alt="Image of first captcha text" width="200" height="auto">
### Stage 2 : Works with CV2
<img src="https://github.com/Lundypgk/Tesseract-API-Captcha/blob/master/testing/captcha3.jpg" alt="Image of first captcha text" width="200" height="auto"><img src="https://github.com/Lundypgk/Tesseract-API-Captcha/blob/master/testing/captcha4.JPG" alt="Image of first captcha text" width="200" height="auto">
### Stage 3 : Does not work 
<img src="https://github.com/Lundypgk/Tesseract-API-Captcha/blob/master/testing/captcha2.JPG" alt="Image of first captcha text" width="200" height="auto">

## To set up
1. Ensure that you have installed [PyTesseract](https://github.com/UB-Mannheim/tesseract/wiki)
2. Ensure that you also have pip installed PyTesseract via "pip install pytesseract"
3. Ensure that you also have pip installed opencvy via "pip install opencv-python"
4. To run enter "python Tesseract.py" in your terminal and input the url to the image
