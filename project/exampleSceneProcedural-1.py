import stickProcedural as sp
import numpy as np

sceneName = 'Hello there-1'

# --------------------------------------------
# create Jason character and add to scene file
# --------------------------------------------
Jason_time = 0.0
Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot = sp.createCharacter(sceneName, 'Jason', 450)
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)

# -------------------------
# wave Jason's left forearm
# -------------------------
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/2)
Jason_time += 10
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)

# ---------------------
# render scene to video
# ---------------------
writer = sp.Render(sceneName)
writer.run()
# writer.write_first_frame()
# writer.show_first_frame()
