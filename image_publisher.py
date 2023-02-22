#!/usr/bin/env python3
# license removed for brevity
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import time

def publish_message():
    pub = rospy.Publisher('video_frames', Image, queue_size = 10)
    rospy.init_node('video_pub_py', anonymous=True)
    rate = rospy.Rate(1)

    cap = cv2.VideoCapture(-1)
    br = CvBridge()

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret == True:
            rospy.loginfo('Publishing Video Frame')
            pub.publish(br.cv2_to_imgmsg(frame))

        rate.sleep()

if __name__ == "__main__":
    try:
        publish_message()
    except rospy.ROSInterruptException:
        pass


'''
class ImagePublisher(object):

    def __init__(self):
        self.node_rate = 1
        self.Image_Pub = rospy.Publisher('camera', Image)
        image = cv2.imread('bananashot.jpg')
        #img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #image = tf.image.resize(img1, (256,256))
        self.bridge = CvBridge()

        try:
            self.image_message = self.bridge.cv2_to_imgmsg(image, encoding = "bgr8")
        except CvBridgeError as e:
            print(e)

        time.sleep(5)
        self.Image_Pub.publish(self.image_message)

    def doSmth(self):
        rospy.loginfo('its working!')

    def run(self):
        loop = rospy.Rate(self.node_rate)
        while not rospy.is_shutdown():
            self.doSmth()
            loop.sleep()
'''

'''
bridge = CvBridge() #Create a Bridge

img = cv2.imread('bananashot.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
image = tf.image.resize(img1, (256,256))

def Camera_init():
    rospy.init_node('Camera', anonymous=True)
    Camera_Pub = rospy.Publisher('camera', Image, queue_size=10)
    Camera_Pub.publish(image)

if __name__ == '__main__':
    try:
        Camera_init()
    except rospy.ROSInterruptException:
        pass
    '''