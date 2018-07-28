# bsm_slam

ROS Package w/ launch files for [hector_slam](https://github.com/tu-darmstadt-ros-pkg/hector_slam)

## Run

```bash
cd ~/catkin_ws/
source devel/setup.bash
roslaunch bsm_slam hector_hokuyo.launch
```

## Setup

Create [catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)

**Install**
```bash
cd ~/catkin_ws/src
git clone https://github.com/BSMRKRS/bsm_slam.git
cd ..
rosdep install --from-paths src --ignore-src --rosdistro <ros version>
catkin_make
```

\* [ROS Raspberry Pi Image](https://downloads.ubiquityrobotics.com/pi.html)
