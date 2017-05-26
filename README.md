Simple program that listens to std_msgs/Strings published 
to the 'paramdump' topic.  Upon receiving one that says "dump waypoints", it executes 
the rosparam command to dump the waypoint parameters. This allows those parameters, which contain 
waypoint coordinates, to be persistent.