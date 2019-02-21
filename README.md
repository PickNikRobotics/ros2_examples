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

1. Re-use or create a colcon workspace as an [overlay](https://index.ros.org/doc/ros2/Tutorials/Colcon-Tutorial/#create-an-overlay) of your `~/ros2_ws/` workspace:

First make sure that you have correctly sourced your ROS1 environment and your `~/ros2_ws/` workspace:

Source your ROS1 environment:

        source /opt/ros/kinetic/setup.bash

Source your new ROS2 install: (*Note:* We use `local_setup.bash` rather than `setup.bash` so that our environment changes stack on top of each other rather than overwriting the previous changes)

        source ~/ros2_ws/local_setup.bash

then create your new ovelay

        export COLCON_WS=~/ws_tom2/
        mkdir -p $COLCON_WS
        cd $COLCON_WS

1. Download the required repositories and install any dependencies:

        git clone git@gitlab.com:tomahawkrobotics/picknik/ros2_examples.git
        wstool init src
        wstool merge -t src ros2_examples/example_cmake/example_cmake.rosinstall
        wstool update -t src
        rosdep install --from-paths src --ignore-src --rosdistro crystal

1. Configure and build the workspace:

        cd $COLCON_WS
        colcon build

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
