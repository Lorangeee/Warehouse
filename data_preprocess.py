# -*- coding: utf-8 -*-
"""data_preprocess.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bctOGSAlZwWWt7zMU1yT1VVOJVgVy104
"""

from PIL import Image
import numpy as np

def data_preprocess(img):
  '''this function preprocess the orignial image file into 100*100*1 gray scale image
  And flattern it's every pixel, return the flattern x_i vector
  Arguments:
  img -- image file that in any size and RGB mode

  Return:
  vec --the flattern pixel vector of the image after processed into 100*100*1 grey scale image
  '''
  img = img.resize((100,100),Image.ANTIALIAS) 
  img = img.convert("L")
  imgarray = np.array(img)
  vec = imgarray.reshape(-1)

  return vec

