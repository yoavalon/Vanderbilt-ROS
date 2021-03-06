import sys
import time
import math
from robot import RobotControlClient

# Test Application
HOST = 'localhost'
#HOST = '127.0.0.1'
PORT = 5512

if(len(sys.argv) >= 2):
	HOST = sys.argv[1]
if(len(sys.argv) >= 3):
	PORT = int(sys.argv[2])

print "Using host: " + HOST + " on port: %d" % PORT
	
robotControlClient = RobotControlClient(HOST, PORT)
robotControlClient.connect()

# Move forward at 0.3 meters / second
robotControlClient.moveForward(0.3);
time.sleep(5); # continue moving for 5 seconds

# Start the robot turning CCW at 20 deg / sec
robotControlClient.turnLeft(20.0 * math.pi / 180.0);
time.sleep(5); # continue turning for 5 seconds

# Start the robot turning CW at 20 deg / sec
robotControlClient.turnRight(20.0 * math.pi / 180.0);
time.sleep(5); # continue turning for 5 seconds

# Stop the Robot
robotControlClient.stop()
time.sleep(5); # pause for 5 seconds

# Move forward at 0.3 meters / second
robotControlClient.moveForward(0.3);
time.sleep(3); # continue moving for 3 seconds

# Stop the Robot
robotControlClient.stop()

# Close the connection to the robot
robotControlClient.disconnect()
