import pybullet as p
import pybullet_data
import time

# Connect to simulation
physicsClient = p.connect(p.GUI)  # or p.DIRECT for no GUI

# Load environment
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Load default URDFs
p.setGravity(0, 0, -9.8)
plane_id = p.loadURDF("plane.urdf")

# Load a robot (KUKA robot arm just for test)
robot_id = p.loadURDF("r2d2.urdf", [0, 0, 0.1])

# Run simulation
for _ in range(1000):
    p.stepSimulation()
    time.sleep(1./240.)

# Disconnect
p.disconnect()
