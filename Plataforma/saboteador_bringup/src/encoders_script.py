#!/usr/bin/env python
import RPi.GPIO as GPIO
import os
import time
import rospy
from std_msgs.msg import Int32



#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN) #LF
GPIO.setup(20,GPIO.IN)
GPIO.setup(6,GPIO.IN) #LB
GPIO.setup(5,GPIO.IN)
GPIO.setup(19,GPIO.IN) #RF
GPIO.setup(16,GPIO.IN)
GPIO.setup(11,GPIO.IN) #RB
GPIO.setup(8,GPIO.IN)


contaLF=0
contaLB=0
contaRF=0
contaRB=0



#callbacks
def CuentaA_LF(channel):
    global contaLF
    contaLF+=1


def CuentaA_LB(channel):
    global contaLB
    contaLB+=1


def CuentaA_RF(channel):
    global contaRF
    contaRF+=1


def CuentaA_RB(channel):
    global contaRB
    contaRB+=1

#Interrupciones
GPIO.add_event_detect(21,GPIO.RISING, callback=CuentaA_LF)
#GPIO.add_event_detect(20,GPIO.RISING, callback=CuentaB_LF)
GPIO.add_event_detect(6,GPIO.RISING, callback=CuentaA_LB)
#GPIO.add_event_detect(5,GPIO.RISING, callback=CuentaB_LB)
GPIO.add_event_detect(19,GPIO.RISING, callback=CuentaA_RF)
#GPIO.add_event_detect(16,GPIO.RISING, callback=CuentaB_RF)
GPIO.add_event_detect(11,GPIO.RISING, callback=CuentaA_RB)
#GPIO.add_event_detect(8,GPIO.RISING, callback=CuentaB_RB)


def talker():

    rospy.init_node('encoder_talker', anonymous=True)
    pub_left = rospy.Publisher('motor_left', Int32, queue_size=10)
    pub_right = rospy.Publisher('motor_right', Int32, queue_size=10)
    rate = rospy.Rate(50)
    
    
    while not rospy.is_shutdown():
        rospy.loginfo(contaLF)
        pub_left.publish(contaLF)
        pub_right.publish(contaRF)
        rate.sleep()


#bucle principal
if __name__=='__main__':
    try:     
        talker()
            
    except rospy.ROSInterruptException:
    	#GPIO.cleanup()
        pass
