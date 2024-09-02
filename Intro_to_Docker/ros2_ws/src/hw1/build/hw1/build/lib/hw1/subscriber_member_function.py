import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import time

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'hw1/partb/topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.i = 0

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s" at %s for the %dth time' % (msg.data, time.time (), self.i))
        self.i += 1


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
