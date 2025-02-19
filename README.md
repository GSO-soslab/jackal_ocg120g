# OCG120G - Jackal

This repository contains configurations and source codes for demos presented in course OCG120G at University of Rhode Island.


## Configure for Jackal J3 with Velodyne Lidar

### Basic Jackal System setup
- download the [clearpath noetic OS](https://packages.clearpathrobotics.com/stable/images/latest/noetic-focal/)
- check the [online jackal manual](https://docs.clearpathrobotics.com/docs/ros1noetic/robots/outdoor_robots/jackal/user_manual_jackal/) for vehicle information
- check the [online system configure](https://docs.clearpathrobotics.com/docs/ros1noetic/robots/outdoor_robots/jackal/tutorials_jackal/) to install all the basic ROS packages.

### Velodyne Lidar ROS driver installation
- IP set to 192.168.131.93 through the website configuration
- install driver: `sudo apt-get install ros-noetic-velodyne-driver`

### ocg120g setup
- go to ROS workspace
- `git clone https://github.com/GSO-soslab/jackal_ocg120g`
- install other dependencies: 
```sh
cd ~/Develop/ros/jackal_ws/
rosdep install --from-paths src --ignore-src -y
```
- `catkin build`

### remote setup
- [install ros noetic](http://wiki.ros.org/noetic/Installation/Ubuntu)
- go to ROS workspace: `cd ~/Your_path/jackal_ws`
- install jackal_ocg120g: `git clone https://github.com/GSO-soslab/jackal_ocg120g`
- install other dependencies: `sudo apt-get install ros-noetic-jackal-description`
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
cd ~/Develop/ros/jackal_ws/src/jackal_ocg120g/ocg120g_remote/setup/J3_laptop
source setup_J3_Demo1.sh
```


------------------------

## Configure for Jackal J2 with RealSense

### Basic Jackal System setup
- download the [clearpath noetic OS](https://packages.clearpathrobotics.com/stable/images/latest/noetic-focal/)
- check the [online jackal manual](https://docs.clearpathrobotics.com/docs/ros1noetic/robots/outdoor_robots/jackal/user_manual_jackal/) for vehicle information
- check the [online system configure](https://docs.clearpathrobotics.com/docs/ros1noetic/robots/outdoor_robots/jackal/tutorials_jackal/) to install all the basic ROS packages.

### RealSense ROS driver installation
- install librealsense SDK
```sh
sudo mkdir -p /etc/apt/keyrings
curl -sSf https://librealsense.intel.com/Debian/librealsense.pgp | sudo tee /etc/apt/keyrings/librealsense.pgp > /dev/null

sudo apt-get install apt-transport-https

echo "deb [signed-by=/etc/apt/keyrings/librealsense.pgp] https://librealsense.intel.com/Debian/apt-repo `lsb_release -cs` main" | \
sudo tee /etc/apt/sources.list.d/librealsense.list
sudo apt-get update

sudo apt-get install librealsense2-dkms
sudo apt-get install librealsense2-utils

sudo apt-get install librealsense2-dev
sudo apt-get install librealsense2-dbg
```
- verify installation: Reconnect the Intel RealSense depth camera and run: `realsense-viewer`

- install realsense ros wrap (needs to be from the source)
```sh
cd `/Your_Workspace/src
git clone https://github.com/IntelRealSense/realsense-ros.git
cd realsense-ros/
git checkout ros1-legacy
cd ..

rosdep install --from-paths src --ignore-src -r -y
 
catkin_init_workspace
cd ..
catkin_make clean
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release
catkin_make install
```

- verify the ros wrapper: `roslaunch realsense2_camera rs_camera.launch`

### ocg120g setup
- go to ROS workspace
- `git clone https://github.com/GSO-soslab/jackal_ocg120g`
- install other dependencies: 
```sh
cd ~/Your_Workspace/
rosdep install --from-paths src --ignore-src -y
```
- `catkin_make`

### remote setup
- [install ros noetic](http://wiki.ros.org/noetic/Installation/Ubuntu)
- go to ROS workspace: `cd ~/Your_path/jackal_ws`
- install jackal_ocg120g: `git clone https://github.com/GSO-soslab/jackal_ocg120g`
- install other dependencies: `sudo apt-get install ros-noetic-jackal-description`
- build: `catkin build ocg120g_remote`

### setup network
- Add laptop hostname in Jackal:
    - In laptop terminal: get [Laptop_IP] by typing `hostname -I`; and get [Laptop_Hostname] by typing `hostname`
    - In jackal terminal: `echo '[Laptop_IP] [Laptop_Hostname]' | sudo tee -a /etc/hosts`
- Do the same thing for Jackal hostanme in laptop

### Demo1 for Realsense camera
- In Jackal, launch Realsense camera: `roslaunch ocg120g_bringup bringup_realsense.launch`
- In laptop:
```sh
cd ~/Develop/ros/jackal_ws/src/jackal_ocg120g/ocg120g_remote/setup/J2_laptop
source setup_J2_Demo1.sh
```

------------------------

## Configure for Jackal J1 with Livox Lidar

### Basic Jackal System setup
- download the [clearpath noetic OS](https://packages.clearpathrobotics.com/stable/images/latest/noetic-focal/)
- check the [online jackal manual](https://docs.clearpathrobotics.com/docs/ros1noetic/robots/outdoor_robots/jackal/user_manual_jackal/) for vehicle information
- check the [online system configure](https://docs.clearpathrobotics.com/docs/ros1noetic/robots/outdoor_robots/jackal/tutorials_jackal/) to install all the basic ROS packages.

### Livox Lidar ROS driver installation
- follow instruction to install [Livox-SDK](https://github.com/Livox-SDK/Livox-SDK)
- build ros driver:
```sh
cd ~/Your_Workspace/src
git clone https://github.com/Livox-SDK/livox_ros_driver
catkin build
```

### ocg120g setup
```sh
cd ~/Your_Workspace/src
git clone https://github.com/GSO-soslab/jackal_ocg120g
cd ~/Your_Workspace/
rosdep install --from-paths src --ignore-src -y
catkin build
```

### remote setup
- [install ros noetic](http://wiki.ros.org/noetic/Installation/Ubuntu)
- go to ROS workspace: `cd ~/Your_path/jackal_ws`
- install jackal_ocg120g: `git clone https://github.com/GSO-soslab/jackal_ocg120g`
- install other dependencies: `sudo apt-get install ros-noetic-jackal-description`
- build: `catkin build ocg120g_remote`

### setup network
- Add laptop hostname in Jackal:
    - In laptop terminal: get [Laptop_IP] by typing `hostname -I`; and get [Laptop_Hostname] by typing `hostname`
    - In jackal terminal: `echo '[Laptop_IP] [Laptop_Hostname]' | sudo tee -a /etc/hosts`
- Do the same thing for Jackal hostanme in laptop

### Demo1 for Livox lidar
- In Jackal:
```sh
# launch lidar
roslaunch ocg120g_bringup bringup_livox.launch
# time sync
sudo ptpd -M -i br0 -C
```

- In laptop:
```sh
cd ~/Develop/ros/jackal_ws/src/jackal_ocg120g/ocg120g_remote/setup/J1_laptop
source setup_J1_Demo1.sh
```

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
