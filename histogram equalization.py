# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 23:39:53 2016

@author: user
"""

import sys
import cv2
import numpy as np
from scipy.misc import *
from scipy import linalg


imagePath = "C:/Users/user/Desktop/lets find/amitabh/AB (3).jpg"

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray)
rev = np.hstack((gray,equalized))
# gray=cv2.resize(gray,(100,100),interpolation=cv2.INTER_AREA)
# im2=cv2.resize(im2,(100,100),interpolation=cv2.INTER_AREA)

# X=np.array(gray.flatten())
# mean=np.mean(X,0)
# ma_data=X=mean

cv2.imshow("img",rev)
cv2.waitKey(0)

#U, S, V = linalg.svd(ma_data.transpose(), full_matrices=True)
