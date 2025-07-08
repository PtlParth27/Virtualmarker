
import cv2
import numpy as np
import os
import time
import HandTrackingModule as htm

#############
brushThickness = 15
eraserThickness = 100
#############

folderPath = 'Header'
myList = os.listdir(folderPath)
overlayList = []

for path in myList:
    img = cv2.imread(f'{folderPath}/{path}')
    overlayList.append(img)
    
header = overlayList[0]
drawColor = (255, 255, 255) # white color

detector = htm.handDetector(maxHands=1, complexity=1, trackConfidence=0.6, detectionConfidence=0.6)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1080, 3), np.uint8)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# because, size of all poster is (1080, 720)

while True:
    
    # 1. Import image
    res, img = cap.read()
    img = cv2.resize(img, (1080, 720))
    img = cv2.flip(img, 1)
    
    # 2. Find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        
        # tip of index and middle fingers
        x1, y1 = lmList[8][1], lmList[8][2] # lmList[8][1:]
        x2, y2 = lmList[12][1], lmList[12][2] # lmList[12][1:]
        
        
        # 3. Check which finger are up
        fingers = detector.fingerUps()
        
        
        # 4. If selection Mode - Two finger are up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("Selection mode")
            # Checking for the click
            if y1 < 83:
                if 172 < x1 < 226:
                    header = overlayList[1]
                    drawColor = (0, 0, 255)
                elif 295 < x1 < 349: 
                    header = overlayList[2]
                    drawColor = (0, 128, 0)
                elif 418 < x1 <470:
                    header = overlayList[3]
                    drawColor = (41, 110, 225)
                elif 540 < x1 < 594:
                    header = overlayList[4]
                    drawColor = (51, 196,  255)
                elif 664 < x1 < 716:
                    header = overlayList[5]
                    drawColor = (53, 7,  58)
                elif 785 < x1 < 838:
                    header = overlayList[6]
                    drawColor = (144, 36,  93)
                elif 915 < x1 < 1018:
                    header = overlayList[7]
                    drawColor = (0, 0, 0)
                
            cv2.rectangle(img, pt1=(x1, y1-35), pt2=(x2, y2+35), color=drawColor, thickness=-1)
    
        # 5. If Drawing mode - Index finger is up
        if fingers[1] == True and fingers[2] == False:
            print("Drawing mode") 
            cv2.circle(img, center=(x1, y1), radius=15, color=drawColor, thickness=-1)
            
            if xp == 0 and yp == 0:
                xp, yp = x1, y1  
            
            if drawColor == (0, 0, 0):
                cv2.line(img, pt1=(xp, yp), pt2=(x1, y1), color=drawColor, thickness=eraserThickness)
                cv2.line(imgCanvas, pt1=(xp, yp), pt2=(x1, y1), color=drawColor, thickness=eraserThickness)
            else:
                cv2.line(img, pt1=(xp, yp), pt2=(x1, y1), color=drawColor, thickness=brushThickness)
                cv2.line(imgCanvas, pt1=(xp, yp), pt2=(x1, y1), color=drawColor, thickness=brushThickness)
                
            xp, yp = x1, y1    
    
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, thresh=10, maxval=255, type=cv2.THRESH_BINARY_INV)
    # if pixel<thresh color=(0,0,0) otherwise (255, 255, 255)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)
    
    img[0:84,:] = header[0:84,:]
    cv2.imshow("Virtual Painter", img)
    # cv2.imshow("Canvas", imgCanvas)
    # cv2.imshow("Inv", imgInv)
    
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break
