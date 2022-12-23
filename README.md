# OCG120G - Jackal

This repository contains configurations and source codes for demos presented in course OCG120G at University of Rhode Island.

## Setting Jackal up

First, refer to the [Jackal documentation](https://www.clearpathrobotics.com/assets/guides/kinetic/jackal/index.html) to complete the Jackal setup.

Complete ROS installation for 

Create a ros workspace in home directory.
```bash
mkdir -p ~/ros_ws/src
git clone https://github.com/GSO-soslab/jackal_ocg120g ~/ros_ws/src
```

Install packages necessary for building packages
```bash
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```

Install package dependencies
```bash
cd ~/ros_ws
rosdep install --from-paths src --ignore-src -y
```

Build the packages with `catkin_make`
```bash
cd ~/ros_ws
catkin_make
```

Finally, if _hacking_ the default setup or configuring attachments is desired, add directive for sourcing the top level workspace into [robot-upstart](http://wiki.ros.org/robot_upstart) configuration and attachments if applicable (see [accessories.launch](https://github.com/jackal/jackal_robot/blob/noetic-devel/jackal_bringup/launch/accessories.launch)).
Keep in mind that this step is not necessary.
```bash
sudo nano /etc/ros/setup.bash
```

To control motors individually, you need to use custom jackal and jackal_robot repositories.
- https://github.com/GSO-soslab/jackal
- https://github.com/GSO-soslab/jackal_robot

### Additional configuration

For additional configuration regarding network and time sync, please refer to [Network Setup](docs/setup_network.md) and [Time Sync Setup](docs/time_sync.md).

## Run demos and attachments

### Run attachments

Launch files for running attachiments resides in ocg120g_bringup package.

```bash
roslaunch ocg120g_bringup bringup_livox.launch ## or
roslaunch ocg120g_bringup bringup_realsense.launch ## or
roslaunch ocg120g_bringup bringup_velodyne.launch ## or
roslaunch ocg120g_bringup bringup_zed.launch ## or
roslaunch ocg120g_bringup relay_zed.launch
```

#### Required repositories

|Driver Name|Repository URL|Working Commit hash|Additional information|
|-----------|--------------|-------------------|----------------------|
|Livox Laser|https://github.com/Livox-SDK/livox_ros_driver.git|[880c46a](https://github.com/Livox-SDK/livox_ros_driver/commit/880c46a91aaa602dbecf20e204da4751747b3826)|Requires additional configuration. Refer to [network setup](docs/setup_network.md) and [time sync setup](docs/time_sync.md).|
|Zed Streo Camera|https://github.com/stereolabs/zed-ros-wrapper.git|[1299a1c](https://github.com/stereolabs/zed-ros-wrapper/commit/1299a1c9fd454194f9a36d57d4075af185d603fe)|
|Velodyne|-|Refer [here](https://www.clearpathrobotics.com/assets/guides/melodic/jackal/description.html)|
|Intel Realsense|-|Refer [here](http://wiki.ros.org/RealSense)|

### Run Cartographer demo

Note: This launch file will run move base as well.

Note #2: If you want to change the algorithm for path finding, you need to modify the `jackal_navigation/launch/include/move_base.launch` file in the `jackal` repository.

```bash
roslaunch ocg120g_mapping cartographer.launch
```
