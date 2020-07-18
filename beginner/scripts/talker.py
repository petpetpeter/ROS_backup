#!/usr/bin/env python
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, Vector3
from math import pi

rospy.init_node('move_square_bb8_service_client')
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
move = Twist()


move.linear.x = 0.0
move.linear.y = 0.0
duration = 10
move.angular.z = pi*2/4/duration

pub.publish(move)
rospy.sleep(duration)

move.angular.z = 0
pub.publish(move)