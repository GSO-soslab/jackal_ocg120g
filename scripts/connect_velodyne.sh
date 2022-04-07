#!/bin/bash

sudo socat TCP-LISTEN:8080,fork,reuseaddr TCP:192.168.131.93:80
