# For J2 jackal and laptop


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
# point cloud compression setup
sudo apt install ros-noetic-point-cloud-transport ros-noetic-draco-point-cloud-transport
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