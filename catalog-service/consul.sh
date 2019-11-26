#!/bin/bash

consul agent -bind $PRIVATE_IP_ADDRESS \
    -advertise $PRIVATE_IP_ADDRESS \
    -join consul_server \
    -node $NODE \
    -config-dir /etc/consul.d \
    -data-dir /data \
    -enable-local-script-checks \
    -dns-port 53 
