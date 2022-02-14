#!/usr/bin/env python


import rospy
import rosnode
import rostopic
import roslaunch
import sys


class TopicRelay:
    def __init__(self):
        if not rospy.has_param('~node_from'):
            sys.exit("No 'from' node is given")


        self._node_from = rospy.get_param('~node_from')

        self._blacklist = []
        if rospy.has_param('~blacklist'):
            self._blacklist = rospy.get_param('~blacklist')

        self.relay_topics = set()
        self.launch = None


    def get_topic_list(self):

        published_topics = rostopic.get_topic_list()[0]

        for topic_info in published_topics:
            publisher = topic_info[2]
            topic = topic_info[0]

            if self._node_from in publisher:
                self.relay_topics.add(topic)


    def spawn_relayers(self):
        self.launch = roslaunch.scriptapi.ROSLaunch()
        self.launch.start()
        for topic in self.relay_topics:
            if topic not in self._blacklist:
                node = roslaunch.core.Node('topic_tools', 'relay', args="{0} relay/{0}".format(topic))
                self.launch.launch(node)


    def wait_for_node(self):
        r = rospy.Rate(1)
        while True:
            if self._node_from in rosnode.get_node_names():
                break
            r.sleep()


def main():
    rospy.init_node("topic_relay", anonymous=True)
    obj = TopicRelay()

    obj.wait_for_node()

    obj.get_topic_list()

    obj.spawn_relayers()

    rospy.spin()

if __name__ == "__main__":
    main()