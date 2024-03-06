#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32, Int32

class SubNode:
    def __init__(self):
        self.subscriber = rospy.Subscriber('/RunyuYang', Int32, self.callback)
        self.publisher = rospy.Publisher('/kthfs/result', Float32, queue_size=10)
        self.q = 0.15

    def callback(self, data):
        result = data.data / self.q
        rospy.loginfo("Publishing: {} / {} = {}".format(data.data, self.q, result))
        self.publisher.publish(result)

if __name__ == '__main__':
    rospy.init_node('subnode', anonymous=True)
    subnode = SubNode()
    rospy.spin()
