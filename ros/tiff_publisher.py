#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

def thermal_camera_publisher():
    # Initialize the ROS node
    rospy.init_node('thermal_camera_publisher', anonymous=True)
    
    # Publisher for the thermal image
    pub = rospy.Publisher('/thermal_camera/image_raw', Image, queue_size=10)
    
    # Initialize the CvBridge
    bridge = CvBridge()
    
    # Set up the VideoCapture to use the correct video device (thermal camera)
    cap = cv2.VideoCapture("/dev/video0")
    
    # Set the frame width and height based on your camera's specs
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
    
    # Set the FourCC to 'Y16' for 16-bit grayscale data
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('Y', '1', '6', ' '))
    
    # Disable RGB conversion to keep the raw radiometric data
    cap.set(cv2.CAP_PROP_CONVERT_RGB, 0)
    
    # Set the publishing rate (10 Hz)
    rate = rospy.Rate(10)  # 10 Hz
    
    while not rospy.is_shutdown():
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            rospy.logwarn("Failed to grab frame from the camera")
            continue
        
        # Check if the frame is 16-bit
        if frame.dtype != np.uint16:
            rospy.logwarn("Captured frame is not 16-bit")
            continue
        
        # Convert the OpenCV image (16-bit) to a ROS Image message
        image_message = bridge.cv2_to_imgmsg(frame, encoding="mono16")
        
        # Publish the image message
        pub.publish(image_message)
        
        # Sleep to maintain the loop rate
        rate.sleep()

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        thermal_camera_publisher()
    except rospy.ROSInterruptException:
        pass
