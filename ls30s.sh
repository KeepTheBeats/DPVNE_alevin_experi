#!/bin/bash


#Monitor the experiment. Run "ls" every 30 seconds.

clear
while [ "1" = "1" ]
do
	ls ~/workspace/alevin-svn2/results
	echo
	sleep 30s
done
