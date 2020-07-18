#!/usr/bin/env python                                                           
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import numpy as np
import math
import time


vel_text = '0s0s0'


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)            
    global vel_text
    vel_text = data.data

rospy.init_node('vel_text', anonymous=True)
# Starts a new node                                                                                           
#rospy.init_node('robot_cleaner', anonymous=True)
velocity_publisher = rospy.Publisher('robot_vel', Twist, queue_size=10)
vel_msg = Twist()
rospy.Subscriber("chatter", String, callback)
while not rospy.is_shutdown():
    
    #rospy.sleep(0.25)
    #print(vel_text)
    #print('im alive')
    Velocity = vel_text.split('s')
    if len(Velocity) == 3:
        Vx0 = float(Velocity[0])/100
        Vy0 = float(Velocity[1])/100
        W   = (float(Velocity[2]))/-100
    print('vel x y W =' + str(Vx0)+' '+str(Vy0)+' '+str(W))
    vel_msg.linear.x = Vx0
    vel_msg.linear.y = Vy0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = W
    velocity_publisher.publish(vel_msg)
    

