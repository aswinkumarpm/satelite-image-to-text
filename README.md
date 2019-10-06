# satelite-image-to-text

It is a python django project used for converting image to text using pytesseract library.
It uses the techinque of Optical Character Recognition.

use pip install -r requirement.tx to install libraries including django.


First you should install binary:
On Linux
sudo apt update

sudo apt install tesseract-ocr

sudo apt install libtesseract-dev


On Mac

brew install tesseract

On Windows

download binary from https://github.com/UB-Mannheim/tesseract/wiki. 

then add pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' to your script.

Then you should install python package using pip:
pip install tesseract
pip install tesseract-ocr
references: https://pypi.org/project/pytesseract/ (INSTALLATION section) and https://github.com/tesseract-ocr/tesseract/wiki#installation
