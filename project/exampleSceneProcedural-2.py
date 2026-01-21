import stickProcedural as sp
import numpy as np

sceneName = 'Hello there-2'

# --------------------------------------------
# create Jason character and add to scene file
# --------------------------------------------
Jason_time = 0.0
Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot = sp.createCharacter(sceneName, 'Jason', 450)
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)

# -------------------------
# wave Jason's left forearm
# -------------------------
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/8)
Jason_time += 0.125
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/8)
Jason_time += 0.125
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/8)
Jason_time += 0.125
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/8)
Jason_time += 0.125
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, -np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, -np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, -np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, -np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, -np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, -np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, -np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, -np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, -np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, -np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)
Jason_left_hand = sp.rotateLimb(Jason_left_elbow, Jason_left_hand, np.pi/6)
Jason_time += 0.25
sp.writeTime(sceneName, 'Jason', str(Jason_time), Jason_right_hand, Jason_right_elbow, Jason_chest, Jason_hips, Jason_head, Jason_left_elbow, Jason_left_hand, Jason_right_foot, Jason_right_knee, Jason_left_knee, Jason_left_foot)

# -------------------------------------------
# create Mark character and add to scene file
# -------------------------------------------
Mark_time = 0.0
Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot = sp.createCharacter(sceneName, 'Mark', 1250)
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)

# -------------------------
# wave Mark's right forearm
# -------------------------
Mark_time += 1.5
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, -np.pi/8)
Mark_time += 0.125
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, -np.pi/8)
Mark_time += 0.125
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, -np.pi/8)
Mark_time += 0.125
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, -np.pi/8)
Mark_time += 0.125
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, -np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, -np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, -np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, -np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, -np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, -np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, -np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_right_hand = sp.rotateLimb(Mark_right_elbow, Mark_right_hand, -np.pi/8)
Mark_time += 0.25
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)
Mark_time += 1
sp.writeTime(sceneName, 'Mark', str(Mark_time), Mark_right_hand, Mark_right_elbow, Mark_chest, Mark_hips, Mark_head, Mark_left_elbow, Mark_left_hand, Mark_right_foot, Mark_right_knee, Mark_left_knee, Mark_left_foot)

# ---------------------
# render scene to video
# ---------------------
writer = sp.Render(sceneName)
writer.run()
