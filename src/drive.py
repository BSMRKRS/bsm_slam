#!/usr/bin/env python
import roslib; roslib.load_manifest('bsm_slam')
import rospy
import tf.transformations
from geometry_msgs.msg import Twist

from pyax12.connection import Connection

# class driveAx:

# def __init__(self, l = (1, 2), r = (3, 4), device='/dev/ttyACM0', baud=1000000):
#     self.sc = Connection(port=device, baudrate=baud)
#     self.L = l
#     self.R = r
#     for i in (l + r):
#         __set_continuous(i)

l = (1, 2)
r = (3, 4)

device = '/dev/ax'
buad = 1000000

def __set_continuous(self, motor_id):
    self.sc.set_cw_angle_limit(motor_id, 0, degrees=False)
    self.sc.set_ccw_angle_limit(motor_id, 0, degrees=False)

def __speedConvert(self, speed):
    if(speed > 0.0):
        speed = 1024 + speed * 1023
        return speed
    elif(speed < 0.0):
        speed = -speed * 1023
        return speed
    else:
        speed = 0
        return speed

def forward(self, speed):
    for i in (self.L + self.R):
        self.sc.set_speed(i, __speedConvert(speed))

def left(self, speed):
    for i in (self.L):
        self.sc.set_speed(i, __speedConvert(speed))

def right(self, sspeed):
    for i in (self.R):
        self.sc.set_speed(i, __speedConvert(speed))

# drive = driveAx()

def drive(x, z):
    if(z > 0):
        right(z)
    elif(z < 0):
        left(z * -1)
    forward(x)

def callback(msg):
    rospy.loginfo("Received a /cmd_vel message!")
    rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))
    drive(msg.linear.x, msg.angular.z)

def listener()):
    rospy.init_node('cmd_vel_listener')
    rospy.Subscriber("/cmd_vel", Twist, self.callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
