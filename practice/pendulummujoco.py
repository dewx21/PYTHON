import time
import mujoco
import mujoco.viewer

# 1. Define the model in MJCF XML format
xml_string = """
<mujoco>
  <option gravity="0 0 -9.81"/>
  <worldbody>
    <!-- Lighting and Floor -->
    <light diffuse=".5 .5 .5" pos="0 0 3" dir="0 0 -1"/>
    <geom type="plane" size="2 2 0.1" rgba=".9 .9 .9 1"/>
    
    <!-- Base Mount -->
    <body name="base" pos="0 0 1.5">
      <geom type="sphere" size="0.05" rgba="1 0 0 1"/>
      
      <!-- Pendulum Pole (Child of Base) -->
      <body name="pole" pos="0 0 0">
        <!-- Hinge joint allows rotation around the Y-axis -->
        <joint name="pivot" type="hinge" axis="0 1 0"/>
        
        <!-- The capsule geom acts as the physical mass and visual pole -->
        <geom type="capsule" fromto="0 0 0  0 0 -1" size="0.04" rgba="0 0.8 0 1" mass="1"/>
      </body>
    </body>
  </worldbody>
</mujoco>
"""

# 2. Load the model and create the dynamic data state
model = mujoco.MjModel.from_xml_string(xml_string)
data = mujoco.MjData(model)

# 3. Set an initial position so the pendulum swings (1 radian)
data.qpos[0] = 1.0 

# 4. Launch the interactive viewer
with mujoco.viewer.launch_passive(model, data) as viewer:
    
    while viewer.is_running():
        step_start = time.time()
        
        # Advance the physics simulation by one timestep
        mujoco.mj_step(model, data)
        
        # Sync the viewer with the new physics state
        viewer.sync()
        
        # Throttle the loop to match real-time
        time_until_next_step = model.opt.timestep - (time.time() - step_start)
        if time_until_next_step > 0:
            time.sleep(time_until_next_step)