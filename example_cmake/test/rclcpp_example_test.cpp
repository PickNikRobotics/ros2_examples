/*********************************************************************
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2018, PickNik LLC
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *   * Neither the name of PickNik LLC nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 *********************************************************************/

/* Author: Stephen Brawner
   Desc: TODO(brawner):
*/

/** EXAMPLES:
    EXPECT_FALSE(robot_state.hasFixedLinks());
    EXPECT_EQ(robot_state.getFixedLinksCount(), 0);
    EXPECT_TRUE(robot_state.getPrimaryFixedLink() == NULL);
    EXPECT_GT(robot_state.getFixedLinksMode(), 0);
    EXPECT_LT( fabs(vars[0] - 0), EPSILON) << "Virtual joint in wrong position " << vars[0];
*/

// ROS
#include <rclcpp/rclcpp.hpp>

// Include class
#include <example_cmake/rclcpp_example.hpp>

// Testing
#include <gtest/gtest.h>

// C++
#include <chrono>
#include <memory>
#include <string>


class RclcppExampleTest : public ::testing::Test
{
public:
  RclcppExampleTest()
  {}

protected:
  rclcpp::Node::SharedPtr nh_;
};  // class RclcppExampleTest


TEST_F(RclcppExampleTest, rclcpp_example_test)
{
  bool test = true;
  EXPECT_TRUE(test);
}

int main(int argc, char ** argv)
{
  testing::InitGoogleTest(&argc, argv);
  // Initialize ROS
  rclcpp::init(argc, argv);
  rclcpp::Logger logger = rclcpp::get_logger("rclcpp_example");
  RCLCPP_INFO(logger, "Starting RclcppExample...");

  // Create a node.
  auto node = std::make_shared<example_cmake::RclcppExample>();

  int result = RUN_ALL_TESTS();
  RCLCPP_INFO(logger, "Test result: " + std::to_string(result));

  rclcpp::shutdown();
  return 0;
}
