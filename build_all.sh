export FASTRTPSGEN_DIR=/usr/local/bin/
export ROS1_DISTRO="kinetic"
export ROS2_DISTRO="crystal"
export ROS1_PATH="/opt/ros/$ROS1_DISTRO/setup.bash"
# TODO:(test local_setup.sh vs setup.sh)
export ROS2_PATH=$HOME/ws_ros2/install/local_setup.bash
export ROS1_WS=$HOME/ws_tom1/
export ROS2_WS=$HOME/ws_tom2/

# Build ROS2 repos except ros1_bridge
source $ROS1_PATH && \
source $ROS2_PATH

cd $ROS2_WS && \
colcon build --symlink-install --packages-skip ros1_bridge --event-handlers console_direct+

cd $ROS1_WS && \
colcon build --cmake-args --symlink-install --event-handlers console_direct+

# Build ROS2 ros1_bridge
source $ROS1_PATH && \
source $ROS1_WS/install/local_setup.bash && \
source $ROS2_PATH && \
source $ROS2_WS/install/local_setup.bash

cd $ROS2_WS
colcon build --symlink-install --packages-select ros1_bridge --cmake-force-configure --event-handlers console_direct+
