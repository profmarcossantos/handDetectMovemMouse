import time
import timeit
import numpy as np
import cv2
import pyautogui
pyautogui.FAILSAFE = False
width , height = pyautogui.size()
xMouse, yMouse = pyautogui.position()
pyautogui.moveTo(width/2,height/2)
minX=width
maxX=0
minY=height
maxY=0
inicio = 0
fim = 0
import sys, getopt
car_cascade = cv2.CascadeClassifier("assets/palm_v4.xml")
car_cascadeClodes = cv2.CascadeClassifier("assets/closed_frontal_palm.xml")
cap = cv2.VideoCapture(0)
while True:
    flag, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hand = car_cascade.detectMultiScale(gray, 1.2, 5)
    handClose = car_cascadeClodes.detectMultiScale(gray, 1.2, 5)
    if handClose == ():
        inicio = 0
        fim = 0
    else:
        if inicio == 0:
            inicio = timeit.default_timer()

    for (x,y,w,h) in handClose:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
        fim = timeit.default_timer()

    closeEyesTime = fim - inicio
    print ('duracao: %f' % (closeEyesTime))
    if closeEyesTime > 3:
        pyautogui.click()
        inicio = timeit.default_timer()
        fim = timeit.default_timer()

    for (x,y,w,h) in hand:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        if minX > x:
            minX = x
        if maxX < x:
            maxX = x
        if minY > y:
            minY = y
        if maxY < y:
            maxY = y
        mediaX = (minX + maxX)/2
        mediaY = (minY + maxY)/2
        if x > mediaX:
            xMouse -=20
        else:
            xMouse +=20
        if y > mediaY:
            yMouse+=10
        else:
            yMouse-=10
        pyautogui.moveTo(xMouse,yMouse)

    frame = cv2.flip(img, 1)
    cv2.imshow('edge', frame)
    ch = cv2.waitKey(5)
    if ch == 27:
        break
cv2.destroyAllWindows()
