import pybullet as p
import pybullet_data
import time

# Connect and set up
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
p.loadURDF("plane.urdf")

# Load the car
car_id = p.loadURDF("car.urdf", [0, 0, 0.1])

# Get joint indices (optional if you know them)
num_joints = p.getNumJoints(car_id)
for i in range(num_joints):
    print(f"Joint {i}: {p.getJointInfo(car_id, i)[1]}")

# Joint names: left_joint = 0, right_joint = 1
LEFT_WHEEL = 0
RIGHT_WHEEL = 1

# 🚗 Control function
def drive_car(left_speed, right_speed):
    p.setJointMotorControl2(car_id, LEFT_WHEEL, p.VELOCITY_CONTROL, targetVelocity=left_speed, force=1)
    p.setJointMotorControl2(car_id, RIGHT_WHEEL, p.VELOCITY_CONTROL, targetVelocity=right_speed, force=1)

# 🧪 Drive loop
for t in range(100000):
    if t < 200:
        drive_car(5, 5)       # move forward
    elif t < 400:
        drive_car(5, -5)      # turn in place
    elif t < 600:
        drive_car(3, 5)       # curve right
    else:
        drive_car(0, 0)       # stop

    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()
