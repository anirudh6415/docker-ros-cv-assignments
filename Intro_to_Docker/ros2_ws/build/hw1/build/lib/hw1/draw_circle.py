import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode (Node):

    def __init__ (self):
        super ().__init__ ("draw_circle")
        self.cmv_vel_pub_ = self.create_publisher (msg_type = Twist, 
                                                   topic = "/turtle1/cmd_vel", 
                                                   qos_profile = 10)
        self.timer_ = self.create_timer (timer_period_sec = 0.5, 
                                          callback = self.send_velocity_command)
        self.get_logger ().info ("Draw cicle started!")

    def send_velocity_command (self):
        msg = Twist ()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmv_vel_pub_.publish (msg)

def main (args = None):
    rclpy.init (args = args)
    node = DrawCircleNode ()
    rclpy.spin (node)
    rclpy.shutdown ()
