cmake_minimum_required(VERSION 3.5)
project(example_cmake)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-W -Wall -Wextra
    -Wwrite-strings -Wunreachable-code -Wpointer-arith
    -Winit-self -Wredundant-decls
    -Wno-unused-parameter -Wno-unused-function)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)


# System dependencies are found with CMake's conventions
find_package(Boost REQUIRED)
find_package(Eigen3 REQUIRED)

# Install Python packages using ament_cmake_python.
ament_python_install_package(${PROJECT_NAME}
  PACKAGE_DIR ${PROJECT_NAME})

###########
## Build ##
###########

# Specify additional locations of header files
# Your package locations should be listed before other locations
include_directories(
  include
  SYSTEM
    ${Boost_INCLUDE_DIR}
    ${EIGEN3_INCLUDE_DIRS}
)

# Adds this packages dependencies to the example_cmake_LIBRARIES and
# example_cmake_INCLUDES CMake variables
ament_export_dependencies(Boost Eigen3)

# Declare a C++ library with project namespace to avoid naming collision
add_library(
  rclcpp_example
  src/rclcpp_example.cpp
)

ament_target_dependencies(rclcpp_example
    "example_interfaces"
    "rclcpp"
    "std_msgs"
    "Boost"
)

ament_export_libraries(rclcpp_example)

# Declare a C++ executable
add_executable(
  rclcpp_example_node
  src/rclcpp_example_node.cpp
)

# Rename C++ executable without namespace
set_target_properties(
  rclcpp_example_node
  PROPERTIES
    OUTPUT_NAME rclcpp_example_node PREFIX ""
)

target_link_libraries(rclcpp_example_node rclcpp_example ${rclcpp_LIBRARIES})

#############
## Install ##
#############

# Mark executables and/or libraries for installation
install(TARGETS rclcpp_example_node
  ARCHIVE DESTINATION lib/${PROJECT_NAME}
  LIBRARY DESTINATION lib/${PROJECT_NAME}
  RUNTIME DESTINATION bin/${PROJECT_NAME})

# Mark cpp header files for installation
install(
  DIRECTORY include/${PROJECT_NAME}
  DESTINATION include/${PROJECT_NAME}
)

# Mark launch files for installation
# install(
#  DIRECTORY launch
#  DESTINATION share/${PROJECT_NAME}
#)

# Mark config files for installation
# install(
#  DIRECTORY
#    config/
#  DESTINATION
#    config/${PROJECT_NAME}
#)

#############
## Testing ##
#############

if(BUILD_TESTING)
  find_package(ament_cmake_gtest REQUIRED)
  find_package(ament_cmake_pytest REQUIRED)
  find_package(ament_lint_auto REQUIRED)

  # ROS2 linters, but disable copyright test. PickNik's copyright's may not conform
  # to this test
  set(ament_cmake_copyright_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()

  # GTests
  ament_add_gtest(example_cmake_test test/rclcpp_example_test.cpp)
  target_link_libraries(example_cmake_test rclcpp_example ${rclcpp_LIBRARIES})


  # Python tests
  ament_add_pytest_test(example_cmake test
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 90)
endif()


#################
## Always Last ##
#################
ament_package()
