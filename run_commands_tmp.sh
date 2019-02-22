export FASTRTPSGEN_DIR=/usr/local/bin/
cd $HOME/src/Firmware
make px4_sitl_rtps gazebo

micrortps_client start -t UDP


#####################################################


export FASTRTPSGEN_DIR=/usr/local/bin/
export ROS1_DISTRO="kinetic"
export ROS2_DISTRO="crystal"
export ROS1_PATH="/opt/ros/$ROS1_DISTRO/setup.bash"
# TODO:(test local_setup.sh vs setup.sh)
export ROS2_PATH=$HOME/ws_ros2/install/local_setup.bash
export ROS1_WS=$HOME/ws_tom1/
export ROS2_WS=$HOME/ws_tom2/

source $ROS1_PATH && \
source $ROS1_WS/install/local_setup.bash && \
source $ROS2_PATH && \
source $ROS2_WS/install/local_setup.bash

micrortps_agent -t UDP



#####################################################


export FASTRTPSGEN_DIR=/usr/local/bin/
export ROS1_DISTRO="kinetic"
export ROS2_DISTRO="crystal"
export ROS1_PATH="/opt/ros/$ROS1_DISTRO/setup.bash"
# TODO:(test local_setup.sh vs setup.sh)
export ROS2_PATH=$HOME/ws_ros2/install/local_setup.bash
export ROS1_WS=$HOME/ws_tom1/
export ROS2_WS=$HOME/ws_tom2/


source $ROS1_PATH && \
source $ROS2_PATH && \
source $ROS2_WS/install/local_setup.bash

export ROS_MASTER_URI=http://localhost:11311

ros2 run ros1_bridge dynamic_bridge


#####################################################


export FASTRTPSGEN_DIR=/usr/local/bin/
export ROS1_DISTRO="kinetic"
export ROS2_DISTRO="crystal"
export ROS1_PATH="/opt/ros/$ROS1_DISTRO/setup.bash"
# TODO:(test local_setup.sh vs setup.sh)
export ROS2_PATH=$HOME/ws_ros2/install/local_setup.bash
export ROS1_WS=$HOME/ws_tom1/
export ROS2_WS=$HOME/ws_tom2/


source $ROS1_PATH && \
source $ROS1_WS/install/local_setup.bash

export ROS_MASTER_URI=http://localhost:11311
roslaunch px4_ros_com sensor_combined_listener.launch


#####################################################


export FASTRTPSGEN_DIR=/usr/local/bin/
export ROS1_DISTRO="kinetic"
export ROS2_DISTRO="crystal"
export ROS1_PATH="/opt/ros/$ROS1_DISTRO/setup.bash"
# TODO:(test local_setup.sh vs setup.sh)
export ROS2_PATH=$HOME/ws_ros2/install/local_setup.bash
export ROS1_WS=$HOME/ws_tom1/
export ROS2_WS=$HOME/ws_tom2/

source $ROS1_PATH && \
source $ROS2_PATH && \
source $ROS2_WS/install/local_setup.bash

sensor_combined_listener