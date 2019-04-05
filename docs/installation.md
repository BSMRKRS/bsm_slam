# Installation/Setup

Installing and setting up SLAM for BSM robotics

[Install](#install) <br>
[Setup Networking](#setup-networking)

## Install

Install ROS

- [ROS Raspberry Pi Image](https://downloads.ubiquityrobotics.com/pi.html)

- [ROS Kinetic Ubuntu Install](http://wiki.ros.org/kinetic/Installation)

Create Catkin Workspace

```bash
source /opt/ros/kinetic/setup.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

Install Dependencies & bsm_slam

```bash
cd ~/catkin_ws/
source devel/setup.bash
cd ~/catkin_ws/src
git clone https://github.com/Slamtec/rplidar_ros.git
git clone https://github.com/ros-perception/slam_gmapping.git
git clone https://github.com/avoss19/bsm_slam.git
cd ~/catkin_ws
catkin_make
```

## Setup Networking

**Pi**

Add these lines to ~/.bashrc

```bash
export ROS_MASTER_URI=localhost:11311
export ROS_HOSTNAME=<Pi IP>
export ROS_IP=<Pi IP>
```

**Laptop**

Add these lines to ~/.bashrc

```bash
export ROS_IP=<Laptop IP>
export ROS_HOSTNAME=<Laptop IP>
export ROS_MASTER_URI=http://<Pi IP>:11311
```
