#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose  # Import the Pose message type from turtlesim package

def pose_callback(data):
    # Callback function to handle incoming pose messages
    x = data.x
    y = data.y
    theta = data.theta

    # Print the position and orientation of the turtle
    rospy.loginfo("Turtle Pose - X: %f, Y: %f, Theta: %f", x, y, theta)

def turtle_pose_subscriber():
    # Initialize the ROS node
    rospy.init_node('turtle_pose_subscriber', anonymous=True)

    # Subscribe to the 'pose' topic with the Pose message type and specify the callback function
    rospy.Subscriber('turtle1/pose', Pose, pose_callback)

    # Keep the node running until it is shut down externally
    rospy.spin()

if __name__ == '__main__':
    try:
        # Run the subscriber node
        turtle_pose_subscriber()
    except rospy.ROSInterruptException:
        pass

