#!/usr/bin/env bash

source ros2_gitlab_ci/gitlab_ros2.bash >/dev/null
return_value=$?
if [ $return_value != 0 ]
then
  echo "gitlab_ros2.bash setup script failed"
  exit $return_value
fi

colcon build --event-handlers console_direct+
return_value=$?
if [ $return_value != 0 ]
then
  echo "Colcon build failed with errors"
  exit $return_value
fi

colcon test --event-handlers console_direct+
return_value=$?
if [ $return_value != 0 ]
then
  echo "Colcon test failed with errors"
  exit $return_value
fi

echo "Build succeeded and tests passed!"
exit 0
