# Config

How to config SLAM

[Change Robot Dimensions](#change-robot-dimensions)
[Change Velocity](#change-velocity)
[Chnage Max Distance of Waypoint Following](#change-max-distance-of-waypoint-following)

## Change Robot Dimensions

Edit: `config/costmap_common_params.yaml`
Change: `footprint` variable

**Note:**
- Footprint is the coordinates of the robot in meters with the LIDAR being the origin

## Change Velocity

Edit: `config/trajectory_planner.yaml`

**Note:**
- Max velocity is 1

## Change Max Distance of Waypoint Following

Edit: `global_costmap_params.yaml` & `local_costmap_params`
