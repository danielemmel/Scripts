#!/usr/bin/env bash

prefix="/mnt/c/"
# remove windows C:\ directory prefix
input=$(echo $1 |cut -c 4-)
# replace \ with / for Linux syntax
output=${input//\\//}
# output WSL windows dir prefix + dir path on WSL surronded by double quotes to make sure it can be used in cd
output=\"$(printf "%s%s" $prefix "$output")\"
echo $output
