# bsm_slam (WIP)

ROS package for bsm robotic's slam. Only tested on ROS Kinetic w/ Ubuntu 16.04

## Installation

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
git clone https://github.com/tu-darmstadt-ros-pkg/hector_slam.git
git clone https://github.com/Slamtec/rplidar_ros.git # RPLIDAR
git clone https://github.com/ros-drivers/urg_node.git # Hokuyo
git clone https://github.com/paulbovbel/frontier_exploration.git
git clone https://github.com/avoss19/bsm_slam.git
cd ~/catkin_ws
catkin_make
```

## Run

**Raspberry Pi & Laptop**

Raspberry Pi & Laptop:

```bash
export ROS_HOSTNAME=<raspberry pi ip>
export ROS_MASTER_URI=http://<raspberry pi ip>
```

Continue to Hokuyo or RPLIDAR

**Hokuyo:**

Each in different window/instance, but you must source each window before each command
​	ex. `source devel/setup.bash`

```bash
rosrun urg_node urg_node

roslaunch bsm_slam hector_hokuyo.launch
```

**RPLIDAR:**

Each in different window/instance, but you must source each window before each command
​	ex. `source devel/setup.bash`

```bash
roslaunch rplidar_ros view_rplidar.launch

roslaunch bsm_slam hector_hokuyo.launch
```
