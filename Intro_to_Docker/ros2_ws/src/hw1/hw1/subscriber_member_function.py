import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import time

# Use this https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')

        # Fill the create_subscription arguments
        self.subscription = self.create_subscription(String,
            'topic',
            self.listener_callback,
            10)

        self.subscription  # prevent unused variable warning
        self.i = 0

    def listener_callback(self, msg):
        # Fill here: Print the message received, time at which it is received and the number of times it is rceived.
        self.get_logger().info('I heard: "%s"' % msg.data)
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
