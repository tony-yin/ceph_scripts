#! /bin/bash
osd_id=$1
ceph osd out osd.$osd_id
/etc/init.d/ceph stop osd.$osd_id
ceph osd crush remove osd.$osd_id
ceph auth del osd.$osd_id
ceph osd rm $osd_id
# 清空 ceph.conf
