
To create an in-vehicle network, configure mini pc as a router.
Install `dnsmasq` software using `apt`.

```bash
sudo apt install dnsmasq
```

> Make sure that there is an active internet connection.

Create a file in directory `/etc/dnsmasq.d` called `soslab.conf`

```
# Set the interface on which dnsmasq operates.
interface=br0

# To disable dnsmasq's DNS server functionality.
port=0

# To enable dnsmasq's DHCP server functionality.
dhcp-range=192.168.131.50,192.168.131.150,255.255.255.0,12h

# Set static IPs of other PCs and the Router.
# This is velodyne
dhcp-host=60:76:88:38:8a:dd,iptime,192.168.131.93,infinite     # Router
# This is jetson
dhcp-host=48:b0:2d:2f:72:35,iptime,192.168.131.119,infinite     # Router
dhcp-host=34:d2:62:a4:6d:ec,iptime,192.168.131.120,infinite     # Router



# Logging.
log-facility=/var/log/dnsmasq.log   # logfile path.
log-async
log-queries # log queries.
log-dhcp    # log dhcp related messages.
```

Create systemd unit in directory `/etc/systemd/system` called `dnsmasq.service`

```
[Unit]
Description=DHCP and DNS caching server for %i.
After=network.target

[Service]
ExecStart=/usr/sbin/dnsmasq -k --conf-file=/etc/dnsmasq.d/soslab.conf
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Reload systemd daemons.

```
sudo systemctl daemon-reload
```

Enable the unit

```bash
sudo systemctl enable dnsmasq
```