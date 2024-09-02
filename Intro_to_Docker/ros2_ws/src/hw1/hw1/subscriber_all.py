import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import time

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('subscriber_all')

        # Fill name and count subscriber
        self.subscription_name = self.create_subscription(
            String,
            'topic',
            self.callback_name,
            10)
        self.subscription_count = self.create_subscription(
            String,
            "topic1",
            self.callback_count,
            10)

        self.subscription_name  # prevent unused variable warning
        self.subscription_count  # prevent unused variable warning
        
        # Global variable to maintain last read message
        self.name = ''
        self.count = 0

    def callback_name(self, msg):
        # Fill the code here to update global variable self.name with message
        self.name = msg.data
        self.get_logger().info('I heard:' + self.name)

    def callback_count(self, msg1):
        self.count = msg1.data
        self.get_logger().info('I heard:' + self.count)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
