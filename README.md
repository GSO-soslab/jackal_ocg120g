# OCG120G - Jackal

This repository contains configurations and source codes for demos presented in course OCG120G at University of Rhode Island.


## Configure for Jackal with Velodyne Lidar

### Basic Jackal System setup
- download the [clearpath noetic OS](https://packages.clearpathrobotics.com/stable/images/latest/noetic-focal/)
- check the [online jackal manual](https://docs.clearpathrobotics.com/docs/ros1noetic/robots/outdoor_robots/jackal/user_manual_jackal/) for vehicle information
- check the [online system configure](https://docs.clearpathrobotics.com/docs_indoornav_user_manual/base_robot_config/config_install_robot_os) to install all the basic ROS packages.

### Velodyne Lidar ROS driver installation
- IP set to 192.168.131.93 through the website configuration
- install driver: `192.168.131.93`

### ocg120g setup
- go to ROS workspace
- `git clone https://github.com/GSO-soslab/jackal_ocg120g`
- install other dependencies: 
```
cd ~/ros_ws
rosdep install --from-paths src --ignore-src -y
```
- `catkin build`

### remote setup
- [install ros noetic](http://wiki.ros.org/noetic/Installation/Ubuntu)
- go to ROS workspace: `cd ~/Your_path/jackal_ws`
- install jackal_ocg120g: `git clone https://github.com/GSO-soslab/jackal_ocg120g`
- build: `catkin build ocg120g_remote`

### setup network
- Add laptop hostname in Jackal:
    - In laptop terminal: get [Laptop_IP] by typing `hostname -I`; and get [Laptop_Hostname] by typing `hostname`
    - In jackal terminal: `echo '[Laptop_IP] [Laptop_Hostname]' | sudo tee -a /etc/hosts`
- Do the same thing for Jackal hostanme in laptop

### Demo1 for Velodyne lidar
- In Jackal, launch Velodyne Lidar: `roslaunch ocg120g_bringup bringup_velodyne.launch`
- In laptop:
```sh
cd ~/Develop/ros/jackal_ws/src/jackal_ocg120g/ocg120g_remote/setup/J1_laptop
source setup_J1.sh
```


------------------------

## Configure for Jackal with RealSense

### Basic Jackal System setup
- download the [clearpath noetic OS](https://packages.clearpathrobotics.com/stable/images/latest/noetic-focal/)
- check the [online jackal manual](https://docs.clearpathrobotics.com/docs/ros1noetic/robots/outdoor_robots/jackal/user_manual_jackal/) for vehicle information
- check the [online system configure](https://docs.clearpathrobotics.com/docs_indoornav_user_manual/base_robot_config/config_install_robot_os) to install all the basic ROS packages.

------------------------

## Configure for Jackal with Livox Lidar

### Basic Jackal System setup
- download the [clearpath noetic OS](https://packages.clearpathrobotics.com/stable/images/latest/noetic-focal/)
- check the [online jackal manual](https://docs.clearpathrobotics.com/docs/ros1noetic/robots/outdoor_robots/jackal/user_manual_jackal/) for vehicle information
- check the [online system configure](https://docs.clearpathrobotics.com/docs_indoornav_user_manual/base_robot_config/config_install_robot_os) to install all the basic ROS packages.


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
