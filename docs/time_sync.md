Livox Lidar requires time synchronization through PTP server.

Install `ptpd` server.
```bash
sudo apt install ptpd
```

Edit configuration for it. `/etc/default/ptpd`
```
# /etc/default/ptpd

# Set to "yes" to actually start ptpd automatically
START_DAEMON=no

# Add command line options for ptpd
PTPD_OPTS="-M -i br0 -C"
```