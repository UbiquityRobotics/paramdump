#!/usr/bin/env python

## Simple program that listens to std_srv/Trigger messages
## on the /save_waypoints service. Upon receiving one it calles
## the rosparam command to save the waypoint parameters to a file.
## Waypoints are currently saved to ~/waypoints.yaml 

import rospy
import subprocess
from std_srvs.srv import Trigger
from std_srvs.srv import TriggerResponse
from os.path import expanduser


def save_waypoints(req):
    try: 
         home = expanduser("~")
         subprocess.check_output(
             ["rosparam", "dump", home + "/waypoints.yaml", "/waypoint"],
             stderr=subprocess.STDOUT
         )
         # parameter -v after "dump" will give verbose output
    except subprocess.CalledProcessError as cpe:
        return TriggerResponse(False, "Error saving waypoints: %s" % cpe.output)

    return TriggerResponse(True, "")

if __name__ == '__main__':
    rospy.init_node('paramdump')
    rospy.Service('save_waypoints', Trigger, save_waypoints)

    rospy.spin()


