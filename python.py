import time

import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path("bodies.xml")
data = mujoco.MjData(model)
j1_joint = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "j1")
motor = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_ACTUATOR, "j1_motor")

Kp = 10
Ki = 5.0
Kd = 1.0

reference = -90 * 3.14 / 180  # vertical

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        # fill code in here
        print(f"angle = {(data.qpos[j1_joint] * 180 / 3.14):0.2f}")

        error = reference - data.qpos[j1_joint]

        print("error = " + str(error))
        data.ctrl[motor] = Kp * error  # positive corresponds to acw
        print("control = " + str(Kp * error))

        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(model.opt.timestep)
