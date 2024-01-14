#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def turtle_twist_publisher():
    # Initialize the ROS node
    rospy.init_node('turtle_twist_publisher', anonymous=True)

    # Create a publisher for the 'cmd_vel' topic with the Twist message type
    twist_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Set the publishing rate (in Hz)
    rate = rospy.Rate(10)  # 10 Hz

    # Create a Twist message to define linear and angular velocities
    twist_cmd = Twist()
    twist_cmd.linear.x = 0.2  # Linear velocity in the x-axis
    twist_cmd.angular.z = 0.2  # Angular velocity in the z-axis

    while not rospy.is_shutdown():
        # Publish the Twist message
        twist_publisher.publish(twist_cmd)

        # Log the information for debugging
        rospy.loginfo("Publishing Twist Command - Linear: %f, Angular: %f",
                      twist_cmd.linear.x, twist_cmd.angular.z)

        # Sleep to meet the specified publishing rate
        rate.sleep()

if __name__ == '__main__':
    try:
        # Run the publisher node
        turtle_twist_publisher()
    except rospy.ROSInterruptException:
        pass

