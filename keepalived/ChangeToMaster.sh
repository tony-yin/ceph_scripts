#!/bin/bash
for folder in $(ls /vol)
do
    if $(mount | grep $folder -q); then
        umount /vol/$folder > /dev/null
    fi
    device=$(grep $folder /etc/block_map -w | awk '{print $1}')
    mount $device /vol/$folder
done
service nfs-kernel-server start
