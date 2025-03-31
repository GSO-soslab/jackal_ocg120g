# For J1 jackal and laptop

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
- install other dependencies: `sudo apt-get install ros-noetic-jackal-description ros-noetic-joy ros-noetic-point-cloud-transport ros-noetic-point-cloud-transport-plugins`
- build: `catkin build ocg120g_remote`
- source the env: `source ~/.bashrc`

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
