

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
    python3-sphinx \
    stow

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
