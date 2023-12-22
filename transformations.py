import cv2 as cv
import numpy as np

img = cv.imread('Photos/evan.jpg')

cv.imshow('Cat', img)

#Translation
def translate(img, x, y):
    # x is number of pixels to shift on x axis
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) # width, height
    return cv.warpAffine(img, transMat, dimensions)

# -x -> image to the left
# -y -> up
# x -> right
# y -> down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_twice = rotate(rotated, -45)
cv.imshow('Roated Twice', rotated_twice)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
#Shrinking - INTER_AREA
#ENlgarging - INTER_LINEAR OR CUBIC

cv.imshow('resized', resized)

# Flipping
# 0 is flipped on x axis
# 1 over y axis
# -1 both vertically and horizontally
flip = cv.flip(img, -1)
cv.imshow('FLip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)