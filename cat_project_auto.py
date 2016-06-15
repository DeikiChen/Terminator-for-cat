# -*- coding: utf-8 -*-
# 树莓派21号引脚、20号引脚分别接两个舵机，16号引脚接HC-SR501传感器，26号引脚接继电器

import RPi.GPIO as GPIO
import time
import signal
import atexit
import cv2
import thread

GPIO.cleanup()

atexit.register(GPIO.cleanup)
servopin_1=21
servopin_2=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin_1, GPIO.OUT, initial=False)
GPIO.setup(servopin_2, GPIO.OUT, initial=False)
p1= GPIO.PWM(servopin_1,50) #50HZ
p2= GPIO.PWM(servopin_2,50) #50HZ
p1.start(0)
p2.start(0)
time.sleep(2)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)


camera=cv2.VideoCapture(0)
camera.set(3,320)
camera.set(4,240)
firstFrame = None
frame_count=0
area_list=[]


#舵机运行程序
def servo_control(servo_id,angle):
    if servo_id==1:
        i=30
        while i>0:
             p1.ChangeDutyCycle(2.5 + 10 * angle / 180)
             time.sleep(0.02)
             p1.ChangeDutyCycle(0)
             #time.sleep(0.01)
             i=i-1
    if servo_id==2:
        i=15
        while i>0:
             p2.ChangeDutyCycle(2.5 + 10 * angle / 180)
             time.sleep(0.02)
             p2.ChangeDutyCycle(0)
             #time.sleep(0.01)
             i=i-1
def relay(i):
    if i==1:
        time.sleep(0.3)
        if GPIO.input(16)==0:
            print "Allow attack"
            GPIO.output(26,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(26,GPIO.LOW)
            
            
    if i==0:
        GPIO.output(26,GPIO.LOW)
    
#舵机运行线程
try:
    thread.start_new_thread(servo_control,(1,90,))#0~180
    thread.start_new_thread(servo_control,(2,50,)) #50~120
    GPIO.output(26,GPIO.LOW)
    time.sleep(2)
except:
    print "Error:unable to start thread"
    
old_cx=0;
old_cy=0;
count=0;
water_count=0;
while(True):
    water_count=water_count+1
    area_list = []

    ret,frame=camera.read()

    #转成灰阶图并且对其进行高斯模糊
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    frame_count=frame_count+1

    if firstFrame is None :
        firstFrame=gray
        continue

    if frame_count==15:
        firstFrame = gray
        frame_count=0;
        continue

    #计算当前帧与第一帧的不同
    frameDelta=cv2.absdiff(firstFrame,gray)
    thresh=cv2.threshold(frameDelta,25,255,cv2.THRESH_BINARY)[1]

    #扩展阈值图像填充空洞,然后找到阈值图像上的轮廓
    thresh = cv2.dilate(thresh, None, iterations=2)
    (cnts, _ )=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #遍历轮廓
    for c in cnts:
        area=cv2.contourArea(c)
        area_list.append(area)
        if area<2000:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if water_count>60:
        if len(area_list)>0: #判断是否有移动像素
            max_area=max(area_list) #获取最大像素值
            max_index=area_list.index(max_area)
            cnt=cnts[max_index]
            M=cv2.moments(cnt)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])

            cv2.rectangle(frame, (cx, cy), (cx + 4, cy + 4), (0, 0, 255), 2)
            cx=int(cx/2.6)
            cy=int(cy/4+50)
            count=count+1
            if count>5:
                if abs(cx-old_cx)>40 or abs(cy-old_cy)>40:
                    
                    if GPIO.input(16)== 0 :               
                            #print cx,cy
                        thread.start_new_thread(servo_control,(1,150-cx,))
                        thread.start_new_thread(servo_control,(2,cy,))
                        thread.start_new_thread(relay,(1,))                      
                            
                    else :
                        thread.start_new_thread(relay,(0,))
                        print "Prohibiting attacks"
                        
                    count=0
            
		
    cv2.imshow('frame', frame)
	#按键盘“q”结束程序
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
	
        

GPIO.output(26,GPIO.LOW)
GPIO.cleanup()
camera.release()
cv2.destroyAllWindows()


    
