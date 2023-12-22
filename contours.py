import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('BLUR', blur)

canny = cv.Canny(img,125,175)
cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('THRESH', thresh)


contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# contours is a python list of all contours
# hierarchies is the hierarchical representation of contours
# retr list is a list that returns all contours found in img, could return retr_external
# retr_tree is all hierarchical contours
# contour aprox method - CHAIN_APPROX_SIMPLE

print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)