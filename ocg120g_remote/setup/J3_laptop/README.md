# For J3 jackal and laptop



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

### Demo2 for Velodyne lidar

In Jackal:
- launch Velodyne Lidar: `roslaunch ocg120g_bringup bringup_velodyne.launch`
- start maping: `roslaunch ocg120g_mapping cartographer_2d_velodyne.launch`

In remote:
- start visualization: `./setup_J1_velodyne_demo2.sh `

### Demo3 for Velodyne lidar
In Jackal:
- launch Velodyne Lidar: `roslaunch ocg120g_bringup bringup_velodyne.launch`
- start navigation: `roslaunch ocg120g_navigation navigation_whitehall_velodyne.launch` 

In remote:
- go to: `cd /home/soslab/Develop/ros/jackal_ws/src/jackal_ocg120g/ocg120g_remote/setup/J3_laptop`
- start visualization: `./setup_J1_velodyne_demo3.sh `