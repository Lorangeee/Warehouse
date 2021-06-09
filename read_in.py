#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image 
import numpy as np
import data_preprocess
def read_in(dir,y):
  '''this function read in training examples and form the X matrix and Y vector
  Arguments:
  dir -- the direction of image file
  y -- true lable of this image, 0 or 1

  Returns:
  X -- (number_of_features,number_of_examples)
  Y -- true lable vector,(1,number_of_examples)
  '''
  X = np.zeros((10000,12000))
  Y = np.zeros((1,12000))

  for i in range(12000):
    X[:,i] = data_preprocess.data_preprocess(Image.open("%s/%d.jpg"%(dir,i)))
    
  Y = Y + y

  return X,Y
    

