import cv2 as cv

# img = cv.imread('Photos/cat.jpg')

# cv.imshow('Cat', img)

#display videos
capture = cv.VideoCapture('Videos/dog.mp4')
# built in webcam likely would be 0

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

#if letter d is pressed, destroy
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
