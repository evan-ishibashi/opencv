import cv2 as cv

# blur when there is noise on images

img = cv.imread('Photos/evan.jpg')
cv.imshow('evan', img)

#averaging blur

average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur - Each pixel gets a weight

gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

#median blur, instead of average, finds median, usually more effective
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

#bilateral blur = retains edges when blurring
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)