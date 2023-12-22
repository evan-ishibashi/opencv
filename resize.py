import cv2 as cv

# img = cv.imread('Photos/cat.jpg')

# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, videos, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Only for Live Video
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('Videos/dog.mp4')
# built in webcam likely would be 0

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

#if letter d is pressed, destroy
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()