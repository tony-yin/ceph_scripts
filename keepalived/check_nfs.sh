#!/bin/sh
vip=$(grep -A 1 virtual_ipaddress /etc/keepalived/keepalived.conf | grep -v virtual_ipaddress | tr -d [:blank:] | cut -d '/' -f 1)
if ! /sbin/ip addr | grep -q $vip; then
    exit
fi
# check nfs service
/sbin/service nfs-kernel-server status >/dev/null
if [ $? -ne 0 ]; then
    # abnormal, try to restart the nfs service
    /sbin/service nfs-kernel-server restart
    /sbin/service nfs-kernel-server status >/dev/null
    if [ $? -ne 0 ]; then
        # still abnormal
        for folder in $(ls /vol)
        do
            if $(mount | grep $folder -q); then
                umount -f /vol/$folder
            fi
        done
        # stop keepalived service
        /sbin/service keepalived stop
    fi
fi
