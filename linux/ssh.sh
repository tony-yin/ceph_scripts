#! /bin/bash

SOURCEHOST=192.168.1.1
DISTHOST=$1
FILE1=/root/1/1.txt
FILE2=/root/2/2.txt
FILE3=/root/3/3.txt
FOLDER1=/root/1/
FOLDER2=/root/2/
FOLDER3=/root/3/
PASSWORD=123456

sshpass -p $PASSWORD ssh $SOURCEHOST \
    sshpass -p $PASSWORD scp ${FILE1} ${DISTHOST}${FOLDER1} && \
    sshpass -p $PASSWORD scp ${FILE2} ${DISTHOST}${FOLDER2} && \
    sshpass -p $PASSWORD scp ${FILE3} ${DISTHOST}${FOLDER3}
