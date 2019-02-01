from setuptools import find_packages
from setuptools import setup

package_name = 'example_python'
setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),

    # Any files that need to be copied over to install go here with the format
    # [(destination1, [file1, file2]), (destination2, [file3, file4])]
    # package.xml and resource/package_name should always be included
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Install as a python file (not Windows friendly) for
        # $ ros2 run example_python rclpy_example_node
        ('lib/' + package_name, ['scripts/rclpy_example_node.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Stephen Brawner',
    author_email='stephenbrawner@picknik.ai',
    maintainer='Stephen Brawner',
    maintainer_email='stephenbrawner@picknik.ai',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'An example of a pure python package using ament_python. Builds much faster than ' +
        'ament_cmake packages.'
    ),
    license='BSD',
    tests_require=['pytest'],
    # Entry points are bundled into an application and can be run directly from command line
    # $ rclpy_example_node
    # This is Windows friendly
    entry_points={
        'console_scripts': [
            'rclpy_example_node = example_python.main:main',
        ],
    },
)
