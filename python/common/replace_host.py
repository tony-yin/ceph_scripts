#! /usr/bin/python
import sys
import os

print sys.argv
src_host = sys.argv[1]
dist_host = sys.argv[2]
root_dir = os.getcwd()

for (dirpath, dirnames, filenames) in os.walk(root_dir):
    for filename in filenames:
        # Replace file content
        filepath = os.path.join(dirpath, filename)
        with open(filepath, 'r') as f:
            content = f.read()
        if src_host in content:
            content = content.replace(src_host, dist_host)
            with open(filepath, 'w') as f:
                f.write(content)

        # Replace file name
        if src_host in filename:
            new_name = filename.replace(src_host, dist_host)
            os.rename(filepath, os.path.join(dirpath, new_name))
