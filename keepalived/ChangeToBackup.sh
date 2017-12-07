#!/bin/bash
service nfs-kernel-server stop
for folder in $(ls /vol)
do
    if $(mount | grep $folder -q); then
        umount -f /vol/$folder
    fi
done
