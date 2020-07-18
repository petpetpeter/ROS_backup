#!/usr/bin/env python

import mqtt.client as mqtt
import time
import rospy
from std_msgs.msg import String
#import ............
def call_peter(target):
    pub.publish(target)
def call_tung(topic,payload):
    client.publish(topic, payload, qos=0, retain=False)
    print('publish'+payload)
#def send_tung():
#    ........
    
def on_message(client, userdata, message):
   x=message.payload.decode()
   global payload
   payload = x.strip()
   if payload == 'start':
       call_peter('0.0s0.0s1.0')
       print("Message Recieved: "+x)
       print('start')
   elif payload == 'arrive':
       print("Message Recieved: "+x)
       print('arrive')
       call_peter('0.0s1.0s1.0')
   elif payload == 'off':
       time.sleep(2)
       print("Message Recieved: "+x)
       print('off')
       call_peter('0.0s1.0s0.0')
       
   #print(x.strip()=="hi")

######## mqttt #####################################################

broker_url = "103.20.207.171"
broker_port = 1883
payload = 'B'
topic="ldb01/posx"
client = mqtt.Client()
client.on_message = on_message
print(client.connect(broker_url, broker_port))
client.subscribe(topic, qos=0)
#call_tung(topic,payload)
#############################################################
rospy.init_node('mecha',anonymous=True)
pub = rospy.Publisher('target',String,queue_size=10)
#call_peter('0.0s0.0s1.0')
client.loop_forever()
###### rospy ###################################################

#while 1:
#    print('oraora')
#    time.sleep(0.1)
    #call_peter()
    #while satae == 1:
#call_tung()
#    call_tung(topic,payload)
#    print('called tung')
        #if state == 0:
        #    send_tung()
        #    break
