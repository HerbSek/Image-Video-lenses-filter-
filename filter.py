import cv2
import numpy as np

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    raise IOError('Cam cannot be opened')
press_key = -1
while True:
    ret, frame = cam.read()
    height, width = frame.shape[:2]
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame,(int(width/1.3),int(height/1.3)), interpolation=cv2.INTER_AREA)
  
    output = frame
    c = cv2.waitKey(1)
    if c == 27:
        break
    elif c != -1:
        press_key = c
    if press_key == ord('a'):
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        output[:,:,0] = cv2.equalizeHist(output[:,:,0])
        output = cv2.cvtColor(output, cv2.COLOR_YUV2RGB)
    elif press_key == ord('b'):
        matrix = np.array([
            [ 0,  1, 0],
            [ 1,  0, 1],
            [ 0,  1, 0] 
        ]) / 2
        output = cv2.filter2D(frame, -1, matrix)
    elif press_key == ord('c'):
        matrix = np.array([
            [-1,-1, -1],
            [-1, 9, -1],
            [-1, -1, -1] 
        ]) 
        output = cv2.filter2D(frame, -1, matrix)
    elif press_key == ord('d'):
        matrix = np.array([
            [ 1, 1, 1],
            [1, -7, 1],
            [1, 1, 1] 
        ]) 
        output = cv2.filter2D(frame, -1, matrix)

    elif press_key == ord('e'):
        matrix = np.array([
             [-1,-1, -1,-1,-1],
             [-1, 2,  2, 2,-1],
             [-1, 2,  20, 2,-1],
             [-1, 2,  2, 2,-1],
             [-1,-1, -1,-1,-1] 
        ]) / 18
        output = cv2.filter2D(frame, -1, matrix)
        # output = cv2.cvtColor(output, cv2.COLOR_RGB2YUV)
        # output[:,:,0] = cv2.equalizeHist(output[:,:,0])
        # output = cv2.cvtColor(output, cv2.COLOR_YUV2RGB)
        # output = cv2.cvtColor(output,0)

    elif press_key == ord('f'):
        array = np.ones((3,3),np.uint8)
        output = cv2.dilate(frame, array ,iterations=1)
    elif press_key == ord('g'):
        output = cv2.Canny(frame, 35,250)
    elif press_key == ord('h'):
        output = cv2.Laplacian(frame, cv2.CV_32F)

    
    cv2.imshow('Input', frame)
    cv2.imshow('Output', output)
    
   
cam.release()
cv2.destroyAllWindows()




