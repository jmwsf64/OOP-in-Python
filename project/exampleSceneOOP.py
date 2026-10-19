import numpy as np
import stickObject as so


Jason = so.Jason("Greetings", 450)
Jason.raise_left_forearm(0.5, 4)
Jason.wave_left_forearm(4.0, 4, 4, np.pi / 6)


Mark = so.Mark("Greetings", 1250)
Mark.wait(1.5)
Mark.raise_right_forearm(0.5, 4)
Mark.wave_right_forearm(4.0, 4, 4, np.pi / 8)
Mark.wait(1)


writer = so.Render("Greetings")
writer.run()
