#!/bin/sh

cd $(dirname "$0")

PARASYTE_PATH="/mnt/SDCARD/.userdata/miyoomini/parasyte/lib"
export PYTHONPATH=${PARASYTE_PATH}/python2.7:${PARASYTE_PATH}/python2.7/site-packages:${PARASYTE_PATH}/python2.7/lib-dynload
export PYTHONHOME=${PARASYTE_PATH}/python2.7:${PARASYTE_PATH}/python2.7/site-packages:${PARASYTE_PATH}/python2.7/lib-dynload
export LD_LIBRARY_PATH=${PARASYTE_PATH}:${PARASYTE_PATH}/python2.7/:${PARASYTE_PATH}/python2.7/lib-dynload:$LD_LIBRARY_PATH

eval /mnt/SDCARD/.userdata/miyoomini/parasyte/bin/python /mnt/SDCARD/.userdata/miyoomini/app.py  # >> /mnt/SDCARD/.userdata/miyoomini/hello-miyoo.log 2>&1

unset LD_PRELOAD
