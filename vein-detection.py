from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480),False)
 
time.sleep(0.1)



for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray,(5,5))
    blur2 = cv2.GaussianBlur(blur,(5,5),0) 
    kernel = np.ones((3,3),np.uint8)
    closing = cv2.morphologyEx(blur2, cv2.MORPH_OPEN, kernel)
    th2 =cv2.adaptiveThreshold(closing,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
    opening = cv2.dilate(th2,kernel,iterations =1)
    
    cv2.imshow('Vein Detector System',frame)
    cv2.imshow('Vein Detector System-Detected',opening)
    rawCapture.truncate(0)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
out.release()
cv2.destroyAllWindows()	