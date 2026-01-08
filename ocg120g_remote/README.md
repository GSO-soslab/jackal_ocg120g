# OCG120G tutorial

## system install:

- ubuntu 20.04:

  - [clearpath noetic OS](https://packages.clearpathrobotics.com/stable/images/latest/noetic-focal/)

  - [jackal manual](https://docs.clearpathrobotics.com/docs/ros1noetic/robots/outdoor_robots/jackal/user_manual_jackal/)

  - [system configure](https://docs.clearpathrobotics.com/docs_indoornav_user_manual/base_robot_config/config_install_robot_os)

- J1: administrator@192.168.1.200, password: clearpath, hostname: cpr-j100-0551

- J1 remote: A4:AE:11:E2:2A:42

- J2: administrator@192.168.1.201, hostname: cpr-j100-0604

- J2 remote: A4:AE:12:8A:78:9A

- J3: administrator@192.168.1.202, hostname: cpr-j100-0608

- J3 remote: A4:AE:12:AE:35:35    

- /etc/netplan/60-wireless.yaml 

  ```sh
  network:
    wifis:
      # Replace WIRELESS_INTERFACE with the name of the wireless network device, e.g. wlan0 or wlp3s0
      # Fill in the SSID and PASSWORD fields as appropriate.  The password may be included as plain-text
      # or as a password hash.  To generate the hashed password, run
      #   echo -n 'WIFI_PASSWORD' | iconv -t UTF-16LE | openssl md4 -binary | xxd -p
      # If you have multiple wireless cards you may include a block for each device.
      # For more options, see https://netplan.io/reference/
      wlp2s0:
        optional: true
        access-points:
          soslab:
            password: endeavour2021 
        dhcp4: false 
        dhcp6: false 
        addresses: [192.168.1.200/24]
        nameservers:
          addresses: [192.168.1.1, 8.8.8.8]
        routes:
          - to: default
            via: 192.168.1.1
  
  ```

- verify remote is working: 

  - install jackal on your remote computer:

    `sudo apt-get install ros-noetic-jackal-desktop`

  - setup hostname for both jackal and remote computer

  - setup env: create `setup_env.sh`

  - check data:

    - imu: `/imu/data_raw`
    - gps: `/navsat/fix`
    - odom:`/odometry/filtered`

--------------------

## Setup cartographer in ros noetic
references: 
- [1](https://google-cartographer-ros.readthedocs.io/en/latest/compilation.html)
- [2](https://github.com/cartographer-project/cartographer_ros/issues/1726)

- install dependency:
```sh
# Install the required libraries that are available as debs.
sudo apt-get update
sudo apt-get install -y \
    clang \
    cmake \
    g++ \
    git \
    google-mock \
    libboost-all-dev \
    libcairo2-dev \
    libceres-dev \
    libcurl4-openssl-dev \
    libeigen3-dev \
    libgflags-dev \
    libgoogle-glog-dev \
    liblua5.2-dev \
    libsuitesparse-dev \
    lsb-release \
    ninja-build \
    stow
python3 -m pip install Sphinx

# Install Protocol Buffers and Abseil if available.
# No need to build it ourselves.
case "$(lsb_release -sc)" in
    jammy|bullseye)
        sudo apt-get install -y libgmock-dev protobuf-compiler libabsl-dev ;;
    focal|buster)
        sudo apt-get install -y libgmock-dev protobuf-compiler ;;
    bionic)
        ;;
esac

# setup the workspace
cd ~/Your_Workspace
wstool init src
wstool merge -t src https://raw.githubusercontent.com/cartographer-project/cartographer_ros/master/cartographer_ros.rosinstall
wstool update -t src
# install sources files
sudo rosdep init # may need to delete the file if you want re-init it
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
sudo apt-get install ros-noetic-pcl-ros
# install abseil
src/cartographer/scripts/install_abseil.sh
cd /usr/local/stow
sudo stow absl
cd -
# uninstall the ROS abseil-cpp if need
sudo apt-get remove ros-${ROS_DISTRO}-abseil-cpp

# build
# rmove the cartographer abseil-cpp
'comment out Line 46 from cartographer/package.xml'
catkin build -j$(nproc)
```

--------------------
