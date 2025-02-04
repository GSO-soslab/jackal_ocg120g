### NOTE: make sure all the hostnames all list        ###
###       in /etc/hosts for both jackals and laptops  ###
###       in order to connect to each others          ###

### USAGE: 
###     source setup_demo1.sh       

### the host name of remote jackal name ###
export ROS_MASTER_URI=http://cpr-j100-0608:11311

### Field laptop (soslab-Latitude-5430-Rugged) to control the remote jackal ###
export ROS_IP=192.168.1.173

### source the remote laptop ros workspace
source /home/soslab/Develop/ros/jackal_ws/devel/setup.bash

### launch the viz
roslaunch ocg120g_remote visualize_demo1_J3.launch 
