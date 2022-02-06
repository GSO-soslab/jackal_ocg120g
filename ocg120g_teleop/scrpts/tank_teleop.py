#!/usr/bin/env python

import rospy
from jackal_msgs.msg import Drive
from sensor_msgs.msg import Joy


class TankTeleop:
    def __init__(self):
        self._left_wheel_axis = rospy.get_param('~left_wheel_axis')
        self._right_wheel_axis = rospy.get_param('~right_wheel_axis')

        self._deadman_button = []
        if rospy.has_param('~deadman_button'):
            self._deadman_button = rospy.get_param("~deadman_button")


        self.pub = rospy.Publisher('cmd_drive', Drive, queue_size=10)

        rospy.Subscriber("joy", Joy, self._joy_callback)

    def _joy_callback(self, msg):
        drive_msg = Drive()
        drive_msg.drivers = [0] * 2
        drive_msg.drivers[Drive.LEFT] = msg.axes[self._left_wheel_axis]
        drive_msg.drivers[Drive.RIGHT] = msg.axes[self._right_wheel_axis]
        drive_msg.mode = Drive.MODE_PWM
        self.pub.publish(drive_msg)

def main():
    rospy.init_node("tank_teleop")
    t = TankTeleop()
    rospy.spin()

if __name__ == "__main__":
    main()