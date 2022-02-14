cmake_minimum_required(VERSION 3.0.2)
project(ocg120g_mapping)

find_package(catkin REQUIRED COMPONENTS
  pointcloud_to_laserscan
)

catkin_package()