import cv2 as cv
from cv2 import waitKey
from cv2 import imshow

#button variables
r = 0
g = 0
h = 0
x = 0
s = 0
c = 0
numofPhotos = 1

#Enabling camera
cam = cv.VideoCapture(0)
cam.set(3,640)
cam.set(2,480)
cam.set(10,100)

#videowriter object
result = cv.VideoWriter('CapturedVideo.avi', cv.VideoWriter_fourcc(*'MJPG'),10,(640,480))

#Displaying camera
while True:
    iftrue, frame = cam.read()
    if s :
        result.write(frame)
    if g :
        frame = cv.cvtColor(frame ,cv.COLOR_BGR2GRAY)
    if r :
        frame = cv.rotate(frame, cv.ROTATE_90_CLOCKWISE) 
    if h :
        frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 
    if x :
        grey = cv.cvtColor(frame ,cv.COLOR_BGR2GRAY)
        rotate = cv.rotate(frame, cv.ROTATE_90_CLOCKWISE)
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 
        cv.imshow("Rotated",rotate) 
        cv.imshow("Grey", grey) 
        cv.imshow("hsv",hsv) 
    
    cv.imshow("Video", frame) 
    input = cv.waitKey(1)

    if (input == ord('q')) or (input == ord('Q')) :
        if s :
            cam.release()
            result.release()
        break
    elif (input == ord('r')) or (input == ord('R')) :
        r,g,h = 1,0,0
    elif (input == ord('h')) or (input == ord('H')) :
        h,r,g, = 1,0,0
    elif (input == ord('g')) or (input == ord('G')) :
        g,r,h = 1,0,0
    elif (input == ord('x')) or (input == ord('X')) :
        x,g,r,h = 1,0,0,0
    elif (input == ord('z')) or (input == ord('Z')) :
        cv.destroyAllWindows()
        x,g,r,h = 0,0,0,0
    elif (input == ord('s')) or (input == ord('S')) :
        s = 1
    elif (input == ord('c')) or (input == ord('C')) :
        cv.imwrite(f'Image{numofPhotos}.png',frame)
        numofPhotos+=1
