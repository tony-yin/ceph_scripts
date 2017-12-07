import sys
import do_exec
size = sys.argv[1]
num = sys.argv[2]
mount_info = do_exec('mount')
sys_disk_name = mount_info[5:8]
def parted_disks(num, size, disk):
    for i in range(int(num)):
        do_exec('sgdisk -n {}:0:+{} /dev/{}'.format(i+1, size, disk))
        print 'disk {} partition {} done ...'.format(disk, i+1)
if len(sys.argv) > 3:
    disks = sys.argv[3:]
    for disk in disks:
        if disk == sys_disk_name:
            print '{} is system disk, can\'t be parted!'.format(disk)
        else:
            parted_disks(num, size, disk)
else:
    all_disks = do_exec('lsblk').splitlines()
    for disk in all_disks:
        if (disk.startswith('sd')):
            disk_name = disk.split()[0]
            if disk_name != sys_disk_name:
                parted_disks(num, size, disk)

