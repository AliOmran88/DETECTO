#!/usr/bin/env python3
# license removed for brevity
import rospy
import os
import cv2
from std_msgs.msg import Float32
from sensor_msgs.msg import Image
import numpy as np
import tensorflow as tf
from cv_bridge import CvBridge, CvBridgeError
from keras.models import load_model

path = os.getcwd()
path = os.path.join(path,'models')
path = os.path.join(path, 'CNN_BA.h5')
model = load_model(path)

def recieved_img_callback(image):
    br = CvBridge()
    rospy.loginfo("receiving Video frame")
    current_frame = br.imgmsg_to_cv2(image)
    cv2.imshow("camera", current_frame)
    cv2.waitKey(1)

    img1 = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)
    resized = tf.image.resize(img1, (256,256))

    Prediction = model.predict(np.expand_dims(resized/255, 0))
    rospy.loginfo("Predicted Value ({})".format(Prediction))
    Angle_pub.publish(Prediction)
    #rate.sleep()
    
    if Prediction > 0.5:
        pred = "banana"
    else:
        pred = "apple"
    rospy.loginfo(f"\nPrediction is {pred}")

def servo_init():
    global Angle_pub, rate
    rospy.init_node('servo', anonymous=True)
    rospy.Subscriber("video_frames", Image, recieved_img_callback)
    Angle_pub = rospy.Publisher('servo', Float32, queue_size=10)
    #rate = rospy.Rate(100)
    rospy.spin()
    

    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        servo_init()
    except rospy.ROSInterruptException:
        pass