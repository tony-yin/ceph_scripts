# ceph_scripts

本项目主要收集一些`ceph`开发过程中用到的脚本或代码，或者是其他一些有用的小工具等等，比如批量分区，批量删除`OSD`等等。

## 技术范围

围绕`ceph`周边的各种应用，还有跟存储相关的技术。

## 收集目的：

* 汇总平常用到的脚本或工具
* 分享出来方便别人，节约时间
* 共同讨论，一起完善优化
* 为同道中人提供接触和扩展的场景

如果大家有兴趣添瓦加砖的话，欢迎补充和提交`PR`

如果大家觉得有帮助的话，欢迎`STAR`

## 收集列表

### OSD创建和删除

Usage: [OSD创建和删除全过程][14]

* [一键创建OSD][1]
* [一键删除OSD][2]

### 批量创建和删除磁盘分区

Usage：[批量创建和删除磁盘分区脚本][15]

* [批量创建磁盘分区][3]
* [批量删除磁盘分区][4]

### RGW

Usage：[RGW 安装和创建][16]

* [S3测试RGW连接][5]

### Keepalived

Usage：[通过 Keepalived 实现 Ceph RBD 的高可用][17]

* [Keepalived-配置文件][6]
* [Keepalived-监测NFS状态][7]
* [Keepalived-backup触发][8]
* [Keepalived-master触发][9]

### Python

#### Python Oralce

Usage：[Python操作Oracle][18]

* [Python向Oracle中批量插入数据][9]

#### Python profile

Usage: [Python Profile][19]

* [Python cprofile decorator][11]
* [Python cprofile pstats][12]
* [Python cprofile my pstats][13]

[1]: https://github.com/tony-yin/ceph_scripts/blob/master/ceph/osd/one_step_create_osd.sh
[2]: https://github.com/tony-yin/ceph_scripts/blob/master/ceph/osd/one_step_delete_osd.sh
[3]: https://github.com/tony-yin/ceph_scripts/blob/master/disks/batch_create_disk_partition.py
[4]: https://github.com/tony-yin/ceph_scripts/blob/master/disks/batch_delete_disk_partition.py
[5]: https://github.com/tony-yin/ceph_scripts/blob/master/ceph/rgw/s3test.py
[6]: https://github.com/tony-yin/ceph_scripts/blob/master/keepalived/keepalived.conf
[7]: https://github.com/tony-yin/ceph_scripts/blob/master/keepalived/check_nfs.sh
[8]: https://github.com/tony-yin/ceph_scripts/blob/master/keepalived/ChangeToBackup.sh
[9]: https://github.com/tony-yin/ceph_scripts/blob/master/keepalived/ChangeToMaster.sh
[10]: https://github.com/tony-yin/ceph_scripts/blob/master/python/orcale/batch_insert_oracle.py
[11]: https://github.com/tony-yin/ceph_scripts/blob/master/python/profile/cprofile_decorator.py
[12]: https://github.com/tony-yin/ceph_scripts/blob/master/python/profile/pstats.py
[13]: https://github.com/tony-yin/ceph_scripts/blob/master/python/profile/mypstats.py
[14]: http://www.tony-yin.top/2017/09/27/OSD-Create-And-Delete/
[15]: http://www.tony-yin.top/2017/10/02/Batch-Create-And-Delete-Disk-Partition-Script/
[16]: http://www.tony-yin.top/2017/11/08/Ceph-RGW/
[17]: http://www.tony-yin.top/2017/12/07/RBD-HA/
[18]: http://www.tony-yin.top/2017/09/10/Python-Oracle/
[19]: http://www.tony-yin.top/2017/10/10/Python-Profiler/
