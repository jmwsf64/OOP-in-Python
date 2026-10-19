"""
Module containing example classes to edit stick figure scene with an
Object-Oriented programming approach and a `Render` class to create an
`.avi` file of the created scene.
"""

import json
import os

import cv2
import numpy as np


class Person:
    def __init__(self, sceneName: str, charName: str, posx: int, time: float = 0.0) -> None:
        """
        A Person Stick figure class for writing positions at key times.
        Writes to `<sceneName>`.json which can be used with `Render` to
        create the project.

        Parameters
        ----------
        sceneName : str
            Name of scene, file extension automatically appended
        charName : str
            Unique name of this object to identify in scene file
        posx : int
            Starting x-position of Character, should be 0 ≤ posx ≤ 1920
        time : float, optional
            Time that the character appears in the scene, by default 0.0
        """

        # ---------------------
        # functional attributes
        # ---------------------
        self._sceneName = f"{sceneName}.json"
        self._charName = charName
        self._time = time
        self._time_increment = 0.0
        self._angle_increment = None

        # -------------------
        # positions of points
        # -------------------
        self._right_hand = np.array([0 + posx, 413])
        self._right_elbow = np.array([45 + posx, 413])
        self._chest = np.array([90 + posx, 413])
        self._hips = np.array([90 + posx, 340])
        self._head = np.array([90 + posx, 470])
        self._left_elbow = np.array([135 + posx, 413])
        self._left_hand = np.array([180 + posx, 413])
        self._right_foot = np.array([20 + posx, 250])
        self._right_knee = np.array([45 + posx, 290])
        self._left_knee = np.array([135 + posx, 290])
        self._left_foot = np.array([160 + posx, 250])

        # ----------------
        # line connections
        # ----------------
        self._connectivity = [
            ["left_hand", "left_elbow"],
            ["left_elbow", "chest"],
            ["chest", "head"],
            ["chest", "right_elbow"],
            ["right_elbow", "right_hand"],
            ["chest", "hips"],
            ["hips", "left_knee"],
            ["left_knee", "left_foot"],
            ["hips", "right_knee"],
            ["right_knee", "right_foot"],
        ]

        # -----------------------------------------
        # write line connections and initial points
        # -----------------------------------------
        self._write_connectivity()
        self._write_key_time()

    def __str__(self) -> str:
        return f"Hi there! My name is {self._charName}!"

    def _write_connectivity(self) -> None:
        """
        Write connectivity array to named file for Object
        """

        # ----------------------------
        # read scene file if it exists
        # ----------------------------
        if os.path.exists(self._sceneName):
            with open(self._sceneName, "r") as f:
                data = json.load(f)
            if "connections" not in data:
                data["connections"] = {}
        else:
            data = {"connections": {}}

        # -------------------------
        # write connections to data
        # -------------------------
        data["connections"][self._charName] = []
        for line in self._connectivity:
            data["connections"][self._charName].append([line[0], line[1]])

        # -----------------------------
        # clear key times if they exist
        # -----------------------------
        data[self._charName] = {}

        # ------------------------
        # write data to scene file
        # ------------------------
        with open(self._sceneName, "w") as f:
            json.dump(data, f, indent="\t")

    def _write_key_time(self) -> None:
        """
        Write positions of attributes for counter of this object
        """

        # ---------------
        # read scene file
        # ---------------
        with open(self._sceneName, "r") as f:
            data = json.load(f)

        # --------------------
        # add key time to data
        # --------------------
        if self._charName not in data:
            data[self._charName] = {}

        # ------------------------
        # update positions in data
        # ------------------------
        data[self._charName][self._time] = {
            "head": np.rint(self._head).astype(int).tolist(),
            "left_hand": np.rint(self._left_hand).astype(int).tolist(),
            "left_elbow": np.rint(self._left_elbow).astype(int).tolist(),
            "right_hand": np.rint(self._right_hand).astype(int).tolist(),
            "right_elbow": np.rint(self._right_elbow).astype(int).tolist(),
            "chest": np.rint(self._chest).astype(int).tolist(),
            "hips": np.rint(self._hips).astype(int).tolist(),
            "left_knee": np.rint(self._left_knee).astype(int).tolist(),
            "left_foot": np.rint(self._left_foot).astype(int).tolist(),
            "right_knee": np.rint(self._right_knee).astype(int).tolist(),
            "right_foot": np.rint(self._right_foot).astype(int).tolist(),
        }

        # ------------------------
        # write data to scene file
        # ------------------------
        with open(self._sceneName, "w") as f:
            json.dump(data, f, indent="\t")

    def _add_time(self) -> None:
        """
        Add time to counter for this object
        """
        self._time += self._time_increment


class Jason(Person):
    def __init__(self, sceneName: str, posx: int, time: float = 0.0) -> None:
        """
        A Stick figure class for the character Jason for writing
        positions at key times. Writes to `<sceneName>`.json which can
        be used with `Render` to create the project.

        Parameters
        ----------
        sceneName : str
            Name of scene, file extension automatically appended
        posx : int
            Starting x-position of Character, should be 0 ≤ posx ≤ 1920
        time : float, optional
            Time that the character appears in the scene, by default 0.0
        """
        super().__init__(sceneName, "Jason", posx, time)

    def __rotate_left_forearm(self) -> None:
        """
        A function to rotate character left wrist around left elbow by
        `self._angle_increment`
        """

        rotation_mat = np.array([
            [np.cos(self._angle_increment), -np.sin(self._angle_increment)],
            [np.sin(self._angle_increment), np.cos(self._angle_increment)],
        ])
        self._left_hand = self._left_elbow + rotation_mat @ (self._left_hand - self._left_elbow)

    def raise_left_forearm(self, duration: float, keys: int) -> None:
        """
        Starting from a T-Pose, rotate left forearm of person 90 degrees

        Parameters
        ----------
        duration : float
            time duration of the project
        keys : int
            number of times to write a key time during project
        """

        # ---------------
        # loop parameters
        # ---------------
        self._time_increment = duration / keys
        self._angle_increment = np.pi / (2 * keys)

        # ---------------------
        # write four key points
        # ---------------------
        for _ in range(keys):
            self._add_time()
            self.__rotate_left_forearm()
            self._write_key_time()

    def wave_left_forearm(
        self,
        duration: float,
        waves: int,
        keysPerWave: int,
        rotation_angle: float,
    ) -> None:
        """
        Wave left arm back and forth by `rotation_angle`

        Parameters
        ----------
        duration : float
            time duration of the project
        waves : int
            number of full waves of the project
        keysPerWave : int
            number of times to write a key time per wave, must be
            divisible by 4
        rotation_angle : float
            angle of wave in Radians
        """

        # ----------------------------------------
        # time increment and initial hand position
        # ----------------------------------------
        self._time_increment = duration / (waves * keysPerWave)
        keysPerStage = int(keysPerWave / 4)
        positive_rotation_increment = rotation_angle / keysPerStage
        negative_rotation_increment = -positive_rotation_increment

        # -------------------
        # wave hand project
        # -------------------
        for _ in range(waves):
            # --------------------------
            # quarter wave one direction
            # --------------------------
            for _ in range(keysPerStage):
                self._angle_increment = positive_rotation_increment
                self._add_time()
                self.__rotate_left_forearm()
                self._write_key_time()

            # ------------------------
            # half wave back direction
            # ------------------------
            for _ in range(2 * keysPerStage):
                self._angle_increment = negative_rotation_increment
                self._add_time()
                self.__rotate_left_forearm()
                self._write_key_time()

            # ---------------------------------
            # quarter wave to original position
            # ---------------------------------
            for _ in range(keysPerStage):
                self._angle_increment = positive_rotation_increment
                self._add_time()
                self.__rotate_left_forearm()
                self._write_key_time()


class Mark(Person):
    def __init__(self, sceneName: str, posx: int, time: float = 0.0) -> None:
        """
        A Stick figure class for the character Mark for writing
        positions at key times. Writes to `<sceneName>`.json which can
        be used with `Render` to create the project.

        Parameters
        ----------
        sceneName : str
            Name of scene, file extension automatically appended
        posx : int
            Starting x-position of Character, should be 0 ≤ posx ≤ 1920
        time : float, optional
            Time that the character appears in the scene, by default 0.0
        """
        super().__init__(sceneName, "Mark", posx, time)

    def __rotate_right_forearm(self) -> None:
        """
        A function to rotate character right wrist around right elbow by
        `self._angle_increment`
        """
        rotation_mat = np.array([
            [np.cos(self._angle_increment), -np.sin(self._angle_increment)],
            [np.sin(self._angle_increment), np.cos(self._angle_increment)],
        ])
        self._right_hand = self._right_elbow + rotation_mat @ (self._right_hand - self._right_elbow)

    def wait(self, time: float) -> None:
        """
        Character waits for `time` in seconds

        Parameters
        ----------
        time : float
            time duration for character to wait
        """

        self._time_increment = time
        self._add_time()
        self._write_key_time()

    def raise_right_forearm(self, duration: float, keys: int) -> None:
        """
        Starting from a T-Pose, rotate right forearm of person -90 degrees

        Parameters
        ----------
        duration : float
            time duration of the project
        keys : int
            number of times to write a key time during project
        """

        # ---------------
        # loop parameters
        # ---------------
        self._time_increment = duration / keys
        self._angle_increment = -np.pi / (2 * keys)

        # ---------------------
        # write four key points
        # ---------------------
        for _ in range(keys):
            self._add_time()
            self.__rotate_right_forearm()
            self._write_key_time()

    def wave_right_forearm(
        self,
        duration: float,
        waves: int,
        keysPerWave: int,
        rotation_angle: float,
    ) -> None:
        """
        Wave right arm back and forth by `rotation_angle`

        Parameters
        ----------
        duration : float
            time duration of the project
        waves : int
            number of full waves of the project
        keysPerWave : int
            number of times to write a key time per wave
        rotation_angle : float
            angle of wave in Radians
        """

        # ----------------------------------------
        # time increment and initial hand position
        # ----------------------------------------
        self._time_increment = duration / (waves * keysPerWave)
        keysPerStage = int(keysPerWave / 4)
        positive_rotation_increment = -rotation_angle / keysPerStage
        negative_rotation_increment = -positive_rotation_increment

        # -------------------
        # wave hand project
        # -------------------
        for _ in range(waves):
            # --------------------------
            # quarter wave one direction
            # --------------------------
            for _ in range(keysPerStage):
                self._angle_increment = positive_rotation_increment
                self._add_time()
                self.__rotate_right_forearm()
                self._write_key_time()

            # ------------------------
            # half wave back direction
            # ------------------------
            for _ in range(2 * keysPerStage):
                self._angle_increment = negative_rotation_increment
                self._add_time()
                self.__rotate_right_forearm()
                self._write_key_time()

            # ---------------------------------
            # quarter wave to original position
            # ---------------------------------
            for _ in range(keysPerStage):
                self._angle_increment = positive_rotation_increment
                self._add_time()
                self.__rotate_right_forearm()
                self._write_key_time()


class Render:
    def __init__(
        self,
        sceneName: str,
        size=(1080, 1920, 3),
        fps=30,
        displayCharNames=False,
    ) -> None:
        """
        Render an existing stick figure project file to an avi file

        Parameters
        ----------
        sceneName : str
            Name of scene json file and output video
        size : tuple, optional
            Resolution of Video, by default (1080, 1920, 3)
        fps : int, optional
            FPS of video, defaults to 30, by default 30
        displayCharNames : bool, optional
            Place Character names over their heads, by default False
        """

        # ------------------------------
        # assign arguments to attributes
        # ------------------------------
        self.__sceneName = sceneName
        self.__fps = fps
        self.__size = size
        self.__displayCharNames = displayCharNames

        # ---------------------
        # functional attributes
        # ---------------------
        self.__writer = None
        self.__charKeys = {}
        self.__charPoints = {}
        self.__time = 0.0
        self.__maxTime = 0.0
        self.__time_increment = 1.0 / self.__fps
        self.__lineThickness = 2
        self.__headRadius = 25
        self.__frame = None

        # ---------------
        # read scene file
        # ---------------
        with open(f"{sceneName}.json", "r") as f:
            self.__chars = json.load(f)
        self.__connections = self.__chars["connections"]
        self.__chars.pop("connections")

        # ----------------------------------
        # initialize dictionaries for frames
        # ----------------------------------
        self.__init_scene()

    def run(self) -> None:
        """
        Render scene to avi using OpenCV `VideoWriter`. Output file will
        be named `sceneName`.avi where `sceneName` is the value passed
        as the `sceneName` argument when initializating the `Render`
        instance.
        """

        # -------------------
        # define video writer
        # -------------------
        self.__writer = cv2.VideoWriter(
            f"{self.__sceneName}.avi",
            cv2.VideoWriter_fourcc(*"MJPG"),  # type: ignore
            self.__fps,
            (self.__size[1], self.__size[0]),
        )

        # -----------------------
        # loop through timestamps
        # -----------------------
        print("Rendering scene from json file")
        while self.__time < self.__maxTime:
            # print time update to terminal
            if self.__time:  # move cursor up one line and clear
                print("\033\\[1A", end="\x1b[2K")
            print(f"    Writing time: {round(self.__time, 1)} of {self.__maxTime}")

            # add next frame to video
            self.__interpolate_points()
            self.__draw_frame()
            self.__writer.write(self.__frame)  # type: ignore

            # increment
            self.__time += self.__time_increment

        print("Finished rendering project")
        self.__writer.release()

    def write_first_frame(self) -> None:
        """
        Write first frame of scene to jpg file. Output file will be
        named `sceneName`.jpg where `sceneName` is the value passed as
        the `sceneName` argument when initializating the `Render`
        instance.
        """

        self.__interpolate_points()
        self.__draw_frame()
        cv2.imwrite(f"{self.__sceneName}.jpg", self.__frame)  # type: ignore

    def show_first_frame(self) -> None:
        """
        Display first frame of scene using OpenCV
        """

        self.__interpolate_points()
        self.__draw_frame()
        cv2.imshow(self.__sceneName, self.__frame)  # type: ignore
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def __init_scene(self) -> None:
        """
        Initialize scene dictionaries
        """

        for char in self.__chars:
            self.__charKeys[char] = np.array(list(self.__chars[char].keys()), dtype=float)
            self.__maxTime = max(self.__maxTime, max(self.__charKeys[char]))
            self.__charPoints[char] = self.__chars[char][str(self.__time)]

    def __interpolate_points(self) -> None:
        """
        interpolate character points at the next frame time
        """

        # -----------------------------------
        # loop through chars and reset points
        # -----------------------------------
        for char in self.__chars:
            # --------------------------
            # self.time == char key time
            # --------------------------
            if str(self.__time) in self.__chars[char]:
                self.__charPoints[char] = self.__chars[char][str(self.__time)]

            # -----------------------------
            # self.time > max time for char
            # -----------------------------
            elif self.__time > max(self.__charKeys[char]):
                pass

            # ----------------------
            # interpolate each point
            # ----------------------
            else:
                ind = np.searchsorted(self.__charKeys[char], self.__time)
                t0 = self.__charKeys[char][ind - 1]
                t1 = self.__charKeys[char][ind]
                t_ratio = (self.__time - t0) / (t1 - t0)
                for point in self.__charPoints[char]:
                    p0 = self.__chars[char][str(float(t0))][point]
                    p1 = self.__chars[char][str(float(t1))][point]
                    self.__charPoints[char][point][0] = int(p0[0] + t_ratio * (p1[0] - p0[0]))
                    self.__charPoints[char][point][1] = int(p0[1] + t_ratio * (p1[1] - p0[1]))

    def __draw_frame(self) -> None:
        """
        Draw character bodies to image frame
        """

        # -------------------------------
        # reset frame to white background
        # -------------------------------
        self.__frame = self.__frame = np.ones(self.__size, np.uint8) * 255

        # -------------------
        # draw chars on frame
        # -------------------
        for char in self.__chars:
            # ---------
            # draw head
            # ---------
            posx, posy = self.__charPoints[char]["head"]
            self.__frame = cv2.circle(
                self.__frame,
                (int(posx), int(posy)),
                self.__headRadius,
                (0, 0, 0),
                self.__lineThickness,
            )

            # --------------------------
            # draw char names over heads
            # --------------------------
            if self.__displayCharNames:
                self.__frame = cv2.putText(
                    self.__frame,
                    char,
                    (posx - 45, posy + 45),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 0),
                    self.__lineThickness,
                    bottomLeftOrigin=True,
                )

            # ---------
            # draw body
            # ---------
            for line in self.__connections[char]:
                p0 = self.__charPoints[char][line[0]]
                p1 = self.__charPoints[char][line[1]]
                p0_1_0 = p0[1]
                p1_1_0 = p1[1]
                if line[0] == "head":
                    p0[1] -= self.__headRadius
                elif line[1] == "head":
                    p1[1] -= self.__headRadius
                self.__frame = cv2.line(self.__frame, p0, p1, (0, 0, 0), self.__lineThickness)
                self.__charPoints[char][line[0]][1] = p0_1_0
                self.__charPoints[char][line[1]][1] = p1_1_0

        # ----------
        # flip frame
        # ----------
        self.__frame = np.flip(self.__frame, axis=0)
