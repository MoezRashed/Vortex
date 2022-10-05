import cv2 as cv
from cv2 import waitKey
import numpy
#height and width of each image
h = 50
w = 50
#image generation
img1 = numpy.zeros((h,w,3), numpy.uint8)
img1[:,:] = (255,0,0)
img2 = numpy.zeros((h,w,3), numpy.uint8)
img2[:,:] = (0,0,0)
img3 = numpy.zeros((h,w,3), numpy.uint8)
img3[:,:] = (0,255,0)
img4 = numpy.zeros((h,w,3), numpy.uint8)
img4[:,:] = (0,0,255)
#image attaching
h1 = numpy.hstack((img1,img2))
h2 = numpy.hstack((img3,img4))
v  = numpy.vstack((h1,h2))
#image resizing
imgresized = cv.resize(v,(200,200))
#image printing
cv.imshow("Final Image",imgresized)
waitKey(0)