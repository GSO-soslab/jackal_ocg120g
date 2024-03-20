### NOTE: make sure all the hostnames all list        ###
###       in /etc/hosts for both jackals and laptops  ###
###       in order to connect to each others          ###


### the host name of remote jackal name ###
export ROS_MASTER_URI=http://cpr-j100-0551:11311

### the IP of current laptop to control the remote jackal ###
export ROS_IP=192.168.1.178

### launch the viz 
roslaunch ocg120g_remote visualize_demo2_J1.launch
