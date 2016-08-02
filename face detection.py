# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 23:18:22 2016

@author: user
"""

import sys
import cv2

imagePath = "C:/Users/user/Desktop/Mahira.jpg"

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("C:/Users/user/Desktop/lets find/haarcascades/haarcascade_frontalface_default.xml")

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
)

print "Found {0} faces!".format(len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("image",gray)
cv2.waitKey(0)