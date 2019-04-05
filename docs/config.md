# Config

How to config SLAM

[Change Robot Dimensions](#change-robot-dimensions) <br>
[Change Velocity](#change-velocity) <br>
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

Edit: `config/global_costmap_params.yaml` & `config/local_costmap_params`

## Change Motors

Edit: `src/drive.py`
Change Functions: `forward()`, `left()` & `right()`
