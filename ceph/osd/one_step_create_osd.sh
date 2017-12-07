#! /bin/bash
start_time=`date +%s`
echo "start time: `date -d @$start_time "+%Y-%m-%d %H:%M:%S"`"
disk=/dev/$1
osd_id=`ceph osd create`
osd_dir=/data/osd.$osd_id
host=10.16.100.99
bucket=default_$host
echo "osd $osd_id is created ..."
mkdir -p $osd_dir
echo "osd directory: /data/osd.$osd_id is created ..."
mkfs -t ext4 -m 0 $disk
echo "disk $disk is built with ext4 file system ..."
mount -o noatime,user_xattr $disk $osd_dir
echo "device: $disk is mounted on directory: $osd_dir ..."
ceph mon getmap -o /tmp/monmap
ceph-osd -i $osd_id --monmap /tmp/monmap --mkfs --mkjournal
echo "osd $osd_id is initialized ..."
osd_uuid=`ceph-osd -i $osd_id --get-osd-fsid`
cat >> /etc/ceph/ceph.conf <<EOF
[osd.$osd_id]
host = $host
public addr = $host
cluster addr = $host
osd uuid = $osd_uuid
EOF
echo 'ceph config file is configured ...'
service ceph start osd.$osd_id
echo "osd $osd_id start ..."
ceph osd crush add $osd_id 0 pool=default host=$bucket
echo "osd $osd_id is added in crush ..."
echo 'all works done ...'
end_time=`date +%s`
echo "end time: `date -d @$end_time "+%Y-%m-%d %H:%M:%S"`"
time_consuming=$(($end_time - $start_time))
echo "The total time consuming is $time_consuming s"
