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
  - statrt cartographer: `roslaunch ocg120g_mapping cartographer.launch` 
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
  - statrt cartographer: `roslaunch ocg120g_mapping cartographer.launch` 
- Remote side:
  - `roscd ocg120g_remote`
  - `cd setup/J2_laptop`
  - `sh setup_Demo2_J2.sh`  
