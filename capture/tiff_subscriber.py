#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

def image_callback(msg):
    # Initialize CvBridge to convert ROS Image message to OpenCV format
    bridge = CvBridge()

    try:
        # Convert the ROS Image message to a 16-bit OpenCV image
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="mono16")

        # Display the image using OpenCV
        cv2.imshow("Thermal Image", cv_image)
        cv2.waitKey(1)

    except Exception as e:
        rospy.logerr(f"Error converting image: {e}")

def thermal_camera_subscriber():
    # Initialize the ROS node
    rospy.init_node('thermal_camera_subscriber', anonymous=True)
    
    # Subscribe to the thermal image topic
    rospy.Subscriber('/thermal_camera/image_raw', Image, image_callback)
    
    # Keep the node running
    rospy.spin()

if __name__ == '__main__':
    try:
        thermal_camera_subscriber()
    except rospy.ROSInterruptException:
        pass
