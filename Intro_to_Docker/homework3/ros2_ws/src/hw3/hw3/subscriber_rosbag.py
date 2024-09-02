#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import time
import PIL
import json
from torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weights
from torchvision.io import read_image
import torch 
bridge = CvBridge()

# Load the maskrcnn resnet 50 model and the weights here
weights = MaskRCNN_ResNet50_FPN_Weights.COCO_V1
model = maskrcnn_resnet50_fpn(weights=weights, progress=False)

transforms = weights.transforms()
model = model.eval ()

def get_prediction():
    d = read_image ('camera_image.jpeg')
    # Write the code here:
    # Transform the image to the input format
    img = transforms(d).unsqueeze(0)
    # Get the output from model
    output = model(img)
    # Get the classes names
    classes = [weights.meta["categories"][label] for label in output[0]['labels'][:3]]
    # return the found objects
    return classes
class Subscriber (Node):

    def __init__ (self):
        super ().__init__ ("subscriber")
        self.subscription = self.create_subscription (
                Image,
                "/zed/zed_node/right_raw/image_raw_color",# Mention the topic name for rosbag
                self.listener_callback,
                10)
        self.subscription

    def listener_callback (self, msg):
        try:
            pass
            # Read in the images in cv2 format from topic using bridge imgmsg_to_cv2 function
            img = bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        except CvBridgeError as e:
            print (e)
        else:
            pass
            # write cv2 image in a local file 'camera_image.jpeg' using imwrite function
            cv2.imwrite('camera_image.jpeg', img)
        ans = get_prediction () 
        print (ans)

def main (args = None):
    rclpy.init (args = args)
    node = Subscriber()
    rclpy.spin (node)
    node.destroy_node ()
    rclpy.shutdown ()

if __name__ == '__main__':
    main ()

