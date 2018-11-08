#!/usr/bin/env python3
import roslib; roslib.load_manifest('bsm_slam')
import rospy
# import tf.transformations
from geometry_msgs.msg import Twist

from pyax12.connection import Connection

L = (1, 2)
R = (3, 4)

device = '/dev/ttyACM1'
# buad = 1000000

sc = Connection(port='/dev/ttyACM1', baudrate=1000000)

def set_continuous(motor_id):
    sc.set_cw_angle_limit(motor_id, 0, degrees=False)
    sc.set_ccw_angle_limit(motor_id, 0, degrees=False)

for i in (L + R):
    print(i)
    set_continuous(int(i))

def speedConvert(speed):
    if(speed > 0.0):
        speed = 1024 + speed * 1023
        return int(speed)
    elif(speed < 0.0):
        speed = -speed * 1023
        return int(speed)
    else:
        speed = 0
        return int(speed)

def forward(speed):
    print(speed)
    for i in (L):
        sc.set_speed(i, speedConvert(speed))
    for i in (R):
        sc.set_speed(i, speedConvert(-speed))

def left(speed):
    print(speed)
    for i in (L):
        sc.set_speed(i, speedConvert(-speed))
    for i in (R):
        sc.set_speed(i, speedConvert(-speed))

def right(speed):
    print(speed)
    for i in (R):
        sc.set_speed(i, speedConvert(speed))
    for i in (L):
        sc.set_speed(i, speedConvert(speed))

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

def listener():
    rospy.init_node('cmd_vel_listener')
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    forward(0)
    # left(.3)
    listener()
