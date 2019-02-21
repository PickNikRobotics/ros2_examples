# ros2_examples

Description: An example ROS2 package

<img src="https://picknik.ai/images/logo.jpg" width="100">

Developed by Stephen Brawner at [PickNik Consulting](http://picknik.ai/)

TODO(brawner): fix Travis badge:
[![Build Status](https://travis-ci.com/PickNikRobotics/example_cmake.svg?token=o9hPQnr2kShM9ckDs6J8&branch=master)](https://travis-ci.com/PickNikRobotics/example_cmake)

## Install

### Ubuntu Debian

> Note: this package has not been released yet

    sudo apt-get install ros-crystal-example-cmake

and:

    sudo apt-get install ros-crystal-example-python

### Build from Source

These instructions assume you are running on Ubuntu 16.04:

1. [Install ROS1 kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu)

1. [Install ROS2 crystal](https://index.ros.org/doc/ros2/Installation/Linux-Development-Setup/) from source.

1. [Install ROS2 Build Tools](https://index.ros.org/doc/ros2/Installation/Linux-Development-Setup/#install-development-tools-and-ros-tools)

1. [Install Fast RTPS](https://eprosima-fast-rtps.readthedocs.io/en/latest/sources.html#installation-from-sources) from source.

First create a source directory where you will build FastRTPS:

        mkdir ~/src/
        cd ~/src

Clone Fast RTPS:

    git clone git@github.com:eProsima/Fast-RTPS
    mkdir Fast-RTPS/build && cd Fast-RTPS/build

Build (*Note:* In order to compile fastrtpsgen you first need to have [gradle](https://gradle.org/install/) and [java JDK](https://www.oracle.com/technetwork/java/javase/downloads/index.html) installed)

To install Java JDK/JRE and gradle:

    sudo apt-get install default-jre default-jdk gradle

To build and install Fast RTPS:

    cmake -DBUILD_JAVA=ON -DTHIRDPARTY=ON ..
    make -j$(nproc)
    sudo make install

You can verify that FastRTPS was installed correctly, run this in a new terminal:

    fastrtpsgen

If you see the `fastrtpsgen` usage information, you are on the right track!

1. Install MavLink/MAVROS and Gazebo:

We first remove `nodemanager` and install recommended dependencies:

    sudo apt-get remove modemmanager -y
    sudo apt-get install git zip qtcreator cmake build-essential genromfs ninja-build exiftool astyle ant openjdk-8-jdk openjdk-8-jre -y
    # make sure xxd is installed, dedicated xxd package since Ubuntu 18.04 but was squashed into vim-common before
    which xxd || sudo apt install xxd -y || sudo apt-get install vim-common --no-install-recommends -y
    # Required python packages
    sudo apt-get install python-argparse python-empy python-toml python-numpy python-dev python-pip -y
    sudo -H pip install --upgrade pip
    sudo -H pip install pandas jinja2 pyserial pyyaml
    # optional python tools
    sudo -H pip install pyulog

ROS Kinetic includes Gazebo7 by default

    # Dependencies
    sudo apt-get install ros-kinetic-desktop-full protobuf-compiler libeigen3-dev libopencv-dev python-rosinstall python-wstool python-rosinstall-generator python-catkin-tools -y

Create a ROS1 workspace:

    export ROS1_WS=$HOME/ws_tom1
    mkdir -p $ROS1_WS/src
    wstool init $ROS1_WS/src
    cd $ROS1_WS

Download and install MavROS

    rosinstall_generator --upstream mavros | tee /tmp/mavros.rosinstall
    # Get latest released mavlink package
    rosinstall_generator mavlink | tee -a /tmp/mavros.rosinstall
    # Setup workspace & install deps
    wstool merge -t src /tmp/mavros.rosinstall
    wstool update -t src
    # Install MavROS dependencies
    rosdep install --from-paths src --ignore-src --rosdistro kinetic -y

Build MavROS!

    catkin build

1. Install geographiclib datasets:

PX4 requires that we install geographiclib datasets:

    install_geo=$(wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh -O -)
    wget_return_code=$?
    # If there was an error downloading the dependent script, we must warn the user and exit at this point.
    if [[ $wget_return_code -ne 0 ]]; then echo "Error downloading 'install_geographiclib_datasets.sh'. Sorry but I cannot proceed further :("; exit 1; fi
    # Otherwise source the downloaded script.
    sudo bash -c "$install_geo"


1. Install the PX4 Firmware repository



We can now clone PX4/Firmware:

    cd ~/src
    git clone https://github.com/PX4/Firmware.git

1. Re-use or create a colcon workspace as an [overlay](https://index.ros.org/doc/ros2/Tutorials/Colcon-Tutorial/#create-an-overlay) of your `~/ros2_ws/` workspace:

First make sure that you have correctly sourced your ROS1 environment and your `~/ros2_ws/` workspace:

Source your ROS1 environment:

        source /opt/ros/kinetic/setup.bash

Source your new ROS2 install: (*Note:* We use `local_setup.bash` rather than `setup.bash` so that our environment changes stack on top of each other rather than overwriting the previous changes)

        source ~/ros2_ws/local_setup.bash

Then create your new overlay:

        export COLCON2_WS=~/ws_tom2/
        mkdir -p $COLCON_WS
        cd $COLCON_WS/src

1. Download the required repositories and install any dependencies:

        git clone git@gitlab.com:tomahawkrobotics/picknik/ros2_examples.git
        wstool init .
        wstool merge ros2_examples/example_cmake/example_cmake.rosinstall
        wstool update
        # We cannot run rosdep install since ROS2 Crystal has not been released to Debian for Ubuntu16
        # rosdep install --from-paths . --ignore-src --rosdistro crystal

1. Configure and build the workspace:

        cd $COLCON_WS
        colcon build --symlink-install

1. Source the workspace.

        source install/local_setup.bash

## Developers: Quick update code repositories

To make sure you have the latest repos:

    cd $COLCON_WS/src/example_cmake
    git checkout master
    git pull origin master
    cd ..
    wstool merge example_cmake/example_cmake.rosinstall
    wstool update
    rosdep install --from-paths . --ignore-src --rosdistro crystal

## Run

Run rclcpp_example_node
```
ros2 run example_cmake rclcpp_example_node # or
rclcpp_example_node
```

### Run with Debugging

# TODO(brawner) check this actually works
Run rclcpp_example_node with GDB
```
ros2 run --prefix 'gdb -ex run --args' example_cmake rclcpp_example_node
```

Run rclcpp_example_node with Callgrind
```
ros2 run --prefix 'valgrind --tool=callgrind' example_cmake rclcpp_example_node
```

Run rclcpp_example_node with Valgrind
```
ros2 run --prefix 'valgrind --tool=callgrind' example_cmake rclcpp_example_node
```

Run rclpy_example_node with pdb
```
cd $COLCON_WS/src/example_cmake/example_cmake
python3 -m pdb rclcpp_example_node.py
```

## Run Docker

### Prerequisite

You must have a private rsa key `~/.ssh/id_rsa` that is not password protected and is attached to your Github and Bitbucket accounts. You must also have a working installation of `docker`.

1. Navigate to `$COLCON_WS/src/example_cmake/.docker`. You should see the `Dockerfile` recipe in the directory.

1. Build the docker image

        cd $COLCON_WS/src/example_cmake/.docker
        cp ~/.ssh/id_rsa id_rsa && docker build -t example_cmake:crystal-source .; rm id_rsa

1. Run the docker image

    * Without the gui

            docker run -it --rm example_cmake:crystal-source /bin/bash

    * With the gui (tested with Ubuntu native and a Ubuntu VM)

            . ./gui-docker -it --rm example_cmake:crystal-source /bin/bash


## Testing and Linting

To test, use the following command with [colcon](https://colcon.readthedocs.io/en/released/).

    colcon test --packages-select example_cmake
