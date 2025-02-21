### NOTE: make sure all the hostnames all list        ###
###       in /etc/hosts for both jackals and laptops  ###
###       in order to connect to each others          ###


### the host name of remote jackal name ###
export ROS_MASTER_URI=http://cpr-j100-0551:11311

### the IP of current laptop to control the remote jackal ###
export ROS_IP=192.168.1.165

### source the remote laptop ros workspace
source /home/soslab/Develop/ros/jackal_ws/devel/setup.bash

### launch the viz
roslaunch ocg120g_remote visualize_demo1_J1.launch

### transmit dense pointcloud
# rosparam set /draco_listener/point_cloud_transport draco
# roslaunch point_cloud_transport_tutorial start.launch
