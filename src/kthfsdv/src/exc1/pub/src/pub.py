#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def publisher():
    rospy.init_node('number_publisher', anonymous=True)
    # Topic 'RunyuYang'
    pub = rospy.Publisher('RunyuYang', Int32, queue_size=10)
    rate = rospy.Rate(20)  # 20Hz

    k = 0
    n = 4
    while not rospy.is_shutdown():
        rospy.loginfo(k)
        pub.publish(k)
        k += n
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
