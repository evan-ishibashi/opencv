import cv2 as cv
import numpy as np

# focus on parts of image that we want

img = cv.imread('Photos/evan.jpg')
cv.imshow('evan', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image', masked)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

# weird_shape = cv.bitwise_and(img)



cv.waitKey(0)
