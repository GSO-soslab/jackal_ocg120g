### NOTE: make sure all the hostnames all list        ###
###       in /etc/hosts for both jackals and laptops  ###
###       in order to connect to each others          ###

### source remote workspace
source /home/soslab/Develop/ros/jackal_ws/devel/setup.bash

### the host name of remote jackal name ###
export ROS_MASTER_URI=http://cpr-j100-0608:11311

### the IP of current laptop to control the remote jackal ###
export ROS_IP=192.168.1.169

### launch the viz 
roslaunch ocg120g_remote visualize_demo3_J2.launch

