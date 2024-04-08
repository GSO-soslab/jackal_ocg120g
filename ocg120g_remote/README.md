# Tutorial for 2024 Spring 

---

## Demo 1

### Jackal 1 (Realsense + Livox)
- Jackal side: 
  - ssh Jackal: `ssh administrator@192.168.1.100`
  - bringup Realsense and Livox: `roslaunch ocg120g_bringup bringup_sensors.launch`
  - enbale time sync for Livox: `sudo ptpd -M -i br0 -C`
- Remote side:
  - `roscd ocg120g_remote`
  - `cd setup/J1_laptop`
  - `sh setup_Demo1_J1.sh`

### Jackal 2 (Velodyne Lidar)
- Jackal side: 
  - ssh Jackal: `ssh administrator@192.168.1.110`
  - unplug and plug Lidar
  - reboot system: `sudo reboot`
- Remote side:
  - `roscd ocg120g_remote`
  - `cd setup/J2_laptop`
  - `sh setup_Demo1_J2.sh`
  
---

## Demo 2

### Jackal 1 (Realsense + Livox)
- Jackal side: 
  - ssh Jackal: `ssh administrator@192.168.1.100`
  - bringup Realsense and Livox: `roslaunch ocg120g_bringup bringup_sensors.launch`
  - enbale time sync for Livox: `sudo ptpd -M -i br0 -C`
  - statrt cartographer based on sensor: 
    - livox: `roslaunch ocg120g_mapping cartographer_2d_livox.launch` 
    - realsense: `roslaunch ocg120g_mapping cartographer_2d_realsense.launch` 
  - save map: `rosrun map_server map_saver -f place_date`
- Remote side:
  - `roscd ocg120g_remote`
  - `cd setup/J1_laptop`
  - `sh setup_Demo2_J1.sh`

### Jackal 2 (Velodyne Lidar)
- Jackal side: 
  - ssh Jackal: `ssh administrator@192.168.1.110`
  - unplug and plug Lidar
  - reboot system: `sudo reboot`
  - check Lidar Hz: `rostopic hz /velodyne_points`
  - statrt cartographer: `roslaunch ocg120g_mapping cartographer_2d_velodyne.launch` 
- Remote side:
  - `roscd ocg120g_remote`
  - `cd setup/J2_laptop`
  - `sh setup_Demo2_J2.sh`  

---

## Demo 3

### Jackal 1 (Realsense + Livox)
- Jackal side: 
  - ssh Jackal: `ssh administrator@192.168.1.100`
  - bringup Realsense and Livox: `roslaunch ocg120g_bringup bringup_sensors.launch`
  - enbale time sync for Livox: `sudo ptpd -M -i br0 -C`
  - statrt realsense navigation based on sensor: 
    - horn: `roslaunch ocg120g_navigation navigation_horn_realsense.launch` 
    - lippitt: `roslaunch ocg120g_navigation navigation_lippitt_realsense.launch` 
- Remote side:

### Jackal 2 (Velodyne Lidar)
- Jackal Side:


## Fix Issues:

- network access issue: `echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null`