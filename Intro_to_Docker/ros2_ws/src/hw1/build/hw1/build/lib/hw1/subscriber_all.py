import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import time

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription_name = self.create_subscription(
                                    String,
                                    'hw1/partc/name',
                                    self.callback_name,
                                    10)
        self.subscription_count = self.create_subscription(
                                    String,
                                    'hw1/partc/count',
                                    self.callback_count,
                                    10)
        self.subscription_name  # prevent unused variable warning
        self.subscription_count  # prevent unused variable warning
        self.name = ''
        self.count = 0

    def callback_name(self, msg):
        self.name = msg.data
        self.get_logger().info('I heard: name: "%s", count: %s' % (self.name, self.count))

    def callback_count(self, msg):
        self.count = msg.data
        self.get_logger().info('I heard: name: "%s", count: %s' % (self.name, self.count))

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
