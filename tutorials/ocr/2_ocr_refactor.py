#!/bin/env python3.6.5

from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

'''
Trying out the OCR in Python tutorial
'''
tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()[0] # Sets to English

'''
Create two lists. One for our images and one for the text we extract
'''
imgs = []
full_text = []

'''
We use wand to import our pdf file and then convert it to jpeg.
'''
file_pdf = Image(filename="pdf_test2.pdf", resolution=300) # Might run into some errors her
file_jpeg = file_pdf.convert('jpeg')

'''
Loop through the pages of the jpeg and append it to our list as a blob
'''
for img in file_jpeg.sequence:
    img_page = Image(image=img)
    imgs.append(img_page.make_blob('jpeg'))

'''
Loop through our blobs in the imgs list and extract the text.
'''
for i in imgs: 
    txt = tool.image_to_string(
        PI.open(io.BytesIO(i)),
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    full_text.append(txt)