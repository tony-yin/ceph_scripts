import sys
import do_exec
def clean_disk(disk_name):
    print 'disk: {} clean start ...'.format(disk_name)
    do_exec('sgdisk -Zog /dev/{}'.format(disk_name))
    print 'disk: {} clean done ...'.format(disk_name)
mount_info = do_exec('mount')
sys_disk_name = mount_info[5:8]
if len(sys.argv) > 1:
    disks = sys.argv[1:]
    for disk_name in disks:
        if disk_name == sys_disk_name:
            print '{} is system disk, can\'t be clean!'.format(disk_name)
        else:
            clean_disk(disk_name)
else:
    all_disks = do_exec('lsblk').splitlines()
    for disk in all_disks:
        if (disk.startswith('sd')):
            disk_name = disk.split()[0]
            if disk_name != sys_disk_name:
                clean_disk(disk_name)
