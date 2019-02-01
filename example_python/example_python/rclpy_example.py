# Software License Agreement (BSD License)
#
#  Copyright (c) 2018, PickNik LLC
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.
#   * Neither the name of PickNik LLC nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
#
# Author: Stephen Brawner
# Desc: TODO(brawner):

import rclpy
from rclpy import logging

from std_msgs.msg import String

__logger_file_name = 'rclpy_example'


class RclpyExample(object):
    """TODO: Fill in docstring for RclpyExample."""

    def __init__(self):
        super().__init__()
        self._node_name = 'RclpyExample_node'
        self._topic_name = '/RclpyExample_topic'
        rclpy.init()
        self._node = rclpy.create_node(self._node_name)
        self._msg = String('hello world')
        self._publisher = self._node.create_publisher(String, self._topic_name)
        self._logger = logging.get_logger(__logger_file_name)

    def timer_callback(self):
        self._logger.info('{}: Publishing msg #: {}'.format(__logger_file_name, self.msg_count))
        self._publisher.publish(self._msg)
        self.msg_count += 1

    def run_node(self):
        publish_period = 0.1  # 10hz
        self.msg_count = 0
        self.tmr = self._node.create_timer(publish_period, self.timer_callback)


def main():
    """Entry point for cross-platform executable."""
    class_object = RclpyExample()

    try:
        class_object.run_node()
    except Exception:
        pass


if __name__ == '__main__':
    main()
