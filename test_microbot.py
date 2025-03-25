import pybullet as p
import pybullet_data
import time

# Start simulation
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
p.loadURDF("plane.urdf")

# Load your custom bot
bot_id = p.loadURDF("microbot.urdf", [0, 0, 0.1])

# Let it run
for _ in range(100000):
    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()
